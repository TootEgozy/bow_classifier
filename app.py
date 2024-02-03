from flask import Flask, render_template, request
from index import process_learning_data

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
def predict():
    user_input = request.form.get('user_input')
    prediction = f"Prediction for '{user_input}': Spam"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')