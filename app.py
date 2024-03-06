from flask import Flask, render_template, request, jsonify
from index import process_learning_data, classify_input, get_inputs_for_user
import json
from waitress import serve

app = Flask(__name__)

learning_data = {}

@app.before_request
def initialize():
    global learning_data
    if not learning_data:
        learning_data = process_learning_data()
        print('added learning data')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-inputs', methods=['POST'])
def generate_inputs():
    body = request.data.decode('utf-8')
    body_dict = json.loads(body)
    print('got a request from client')
    print(body)
    cls_type = body.get('cls_type')
    count = body.get('count')
    inputs = get_inputs_for_user('spam', 5)
    # return jsonify({'inputs': inputs})
    # new_inputs = ['Input 1', 'Input 2', 'Input 3']
    return jsonify(inputs=inputs)


@app.route('/classifier', methods=['POST'])
def classifier():
    input_text = request.form.get('input_text')
    input_type = request.form.get('input_type')
    cls_result = classify_input(input_text, input_type, learning_data[input_type])

    return render_template('index.html', classification=cls_result)

if __name__ == '__main__':
    # dev server
    # app.run(host='0.0.0.0')
    # production server
    serve(app, host='0.0.0.0', port=5000)
