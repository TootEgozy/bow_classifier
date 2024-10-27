import os

from flask import Flask, request, jsonify
from waitress import serve
from index import process_learning_data, classify_input, get_inputs_for_user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

learning_data = process_learning_data()
print('added learning data')


port = int(os.environ.get("PORT", 5000))

# make sure that learning data is loaded
@app.route('/server_ready', methods=['GET'])
def initialize_learning_data():
    global learning_data
    if not learning_data:
        learning_data = process_learning_data()
        print('added learning data')
        return jsonify({'server_ready': True})
    else:
        return jsonify({'server_ready': True})

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
    if learning_data:
        data = request.get_json()
        input_text = data.get('input_text')
        cls_type = data.get('cls_type')
        cls_result = classify_input(input_text, cls_type, learning_data[cls_type])
        return jsonify(result=cls_result)
    else:
        return jsonify({'error': 'missing learning data'})


if __name__ == '__main__':
    # dev server
    # app.run(host='0.0.0.0', port=5000)
    # production server
    serve(app, host='0.0.0.0', port=port)
