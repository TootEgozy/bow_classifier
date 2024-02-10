import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def answer_templates(category):
    if(category == 'spam'):
        return {
            "spam": "We are {}% certain that your input is spam"
        }

def process_learning_file(filepath, label_index, text_index):
    texts = list()
    labels = list()
    with open(filepath, 'r', encoding='latin1') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            labels.append(row[label_index].strip('"'))
            texts.append(row[text_index].strip('"'))
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(texts)
    return {
        "matrix": matrix,
        "labels": labels,
        "vectorizer": vectorizer
    }

def process_learning_data():
    spam_data = process_learning_file('learning_data/spam.csv', 0, 1)
    sentiment_data = process_learning_file('learning_data/sentiment.csv', 1, 0)
    return {
        'spam': spam_data,
        'sentiment': sentiment_data
    }

def classify_input(input, cls_data):
    input_vec = cls_data['vectorizer'].transform([input])
    X_train, X_test, y_train, y_test = train_test_split(cls_data['matrix'], cls_data['labels'], test_size=0.2, random_state=42)
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)
    predictions_accuracy = classifier.score(X_test, y_test) * 100
    predicted_label = classifier.predict(input_vec)[0]
    return predicted_label, predictions_accuracy


