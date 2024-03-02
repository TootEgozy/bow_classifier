from flask import Flask, render_template, request, jsonify
from index import process_learning_data, classify_input, get_inputs_for_user
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
    # data = request.get_json()
    # print('got a request from client')
    # print(data)
    # cls_type = data.get('cls_type')
    # count = data.get('count')
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
