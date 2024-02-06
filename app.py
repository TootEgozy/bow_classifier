from flask import Flask, render_template, request
from index import process_learning_data, classify_input
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

@app.route('/classifier', methods=['POST'])
def classifier():
    input_text = request.form.get('input_text')
    input_type = request.form.get('input_type')
    cls_result = classify_input(input_text, learning_data[input_type])
    classification = f"classification for '{input_text}': {cls_result[0]}, Accuracy: {cls_result[1]}"

    return render_template('index.html', classification=classification)

if __name__ == '__main__':
    # dev server
    # app.run(host='0.0.0.0')
    # production server
    serve(app, host='0.0.0.0', port=5000)
