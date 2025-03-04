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

@app.before_request
def before_request():
    blocked = request_limiter.check_handle_limit_reached()
    if blocked:
        return make_response(jsonify('requests are blocked'), 429)
    else:
        if learning_data is not None:
            memory_unloader.reset_timer()
        else:
            threading.Thread(target=load_learning_data).start()
            memory_unloader.reset_timer()
            return make_response(jsonify('missing learning data'), 503)


# make sure that learning data is loaded
@app.route('/server_ready', methods=['GET'])
def initialize_learning_data():
    global learning_data
    if not learning_data:
        load_learning_data() # wait for this process
        return jsonify({'server_ready': True}, 200)
    else:
        return jsonify({'server_ready': True}, 200)

# get the cls type and a count from the user and return sample inputs
@app.route('/generate_inputs', methods=['POST'])
def generate_inputs():
    try:
        data = request.get_json()
        cls_type = data.get('cls_type')
        count = data.get('count')
        inputs = get_inputs_for_user(cls_type, count)
        return jsonify(inputs=inputs)
    except Exception as e:
        return jsonify(error=str(e)), 400


# classify input
@app.route('/classify', methods=['POST'])
def index():
    data = request.get_json()
    input_text = data.get('input_text')
    cls_type = data.get('cls_type')
    cls_result = classify_input(input_text, cls_type, learning_data[cls_type])
    return jsonify(result=cls_result)



if __name__ == '__main__':
    # dev server
    app.run(host='0.0.0.0', port=5000)
    # production server
    # serve(app, host='0.0.0.0', port=port)
