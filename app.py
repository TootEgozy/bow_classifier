import os
import threading

from flask import Flask, request, jsonify, make_response
from waitress import serve
from index import process_learning_data, classify_input, get_inputs_for_user
from flask_cors import CORS

from utils.request_limiter import RequestLimiter
from utils.memory_unloader import MemoryUnloader

app = Flask(__name__)
CORS(app)

learning_data = None
learning_data_lock = threading.Lock()
data_loading_thread = None

port = int(os.environ.get("PORT", 5000))
request_limiter = RequestLimiter()
memory_unloader = MemoryUnloader(app)


def load_learning_data():
    global learning_data
    with learning_data_lock:
        learning_data = process_learning_data()
        print('added learning data')

def unload_learning_data():
    global learning_data
    with learning_data_lock:
        learning_data = None
        print("unloaded learning data")

# append these methods to app, so that dependencies can access them
app.config['load_learning_data'] = load_learning_data
app.config['unload_learning_data'] = unload_learning_data

# middleware to check if requests are blocked, resetting the memory_unloader timer,
# and if learning _data is missing load it
@app.before_request
def before_request():
    global learning_data, data_loading_thread
    blocked = request_limiter.check_handle_limit_reached()
    if blocked:
        return make_response(jsonify({"message": "Requests are blocked, please try again later"}), 429)
    else:
        memory_unloader.reset_timer()
        if learning_data is None:
            if data_loading_thread is None or not data_loading_thread.is_alive():
                data_loading_thread = threading.Thread(target=load_learning_data)
                data_loading_thread.start()
            return make_response(jsonify({"message": "Missing learning data"}), 503)


# an endpoint to test if the server is ready, if we reached it then learning data is loaded.
@app.route('/server_ready', methods=['GET'])
def initialize_learning_data():
    return make_response("", 204)

# get the classification type and a count from the user and return sample inputs
@app.route('/generate_inputs', methods=['POST'])
def generate_inputs():
    try:
        data = request.get_json()
        cls_type = data.get('cls_type')
        count = data.get('count')

        if cls_type is None or count is None:
            return make_response(jsonify({"error": "Missing 'cls_type' or 'count'"}), 400)

        inputs = get_inputs_for_user(cls_type, count)
        return make_response(jsonify({"inputs": inputs}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "Internal server error"}), 500)


# classify input from user
@app.route('/classify', methods=['POST'])
def index():
    try:
        data = request.get_json()
        input_text = data.get('input_text')
        cls_type = data.get('cls_type')

        if cls_type is None or input_text is None:
            return make_response(jsonify({"error": "Missing 'cls_type' or 'input_text'"}), 400)

        cls_result = classify_input(input_text, cls_type, learning_data[cls_type])
        return make_response(jsonify({"result": cls_result}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "Internal server error"}), 500)


if __name__ == '__main__':
    # dev server
    app.run(host='0.0.0.0', port=5000)
    # production server
    # serve(app, host='0.0.0.0', port=port)
