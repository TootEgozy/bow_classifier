import csv

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# TODO: split the huge twitter sentiment dataset and add to the data
def answer_templates(category):
    if(category == 'spam'):
        return {
            "spam": "We are {}% certain that your input is spam"
        }

# TODO: take out the reading files into text / labels logic into a separate function so that files
#  of the same type can be accumulated.
def process_learning_files(filenames, label_index, text_index):
    texts = list()
    labels = list()
    for filename in filenames:
        with open(f'learning_data/{filename}.csv', 'r', encoding='latin1') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                labels.append(row[label_index].strip('"'))
                texts.append(row[text_index].strip('"'))
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(texts)
    print(len(labels))
    return {
        "matrix": matrix,
        "labels": labels,
        "vectorizer": vectorizer
    }

def process_learning_data():
    spam_files = ['spam']
    sentiment_files = ['sentiment_1', 'sentiment_2', 'sentiment_3', 'sentiment_4', 'sentiment_5']
    spam_data = process_learning_files(spam_files, 0, 1)
    sentiment_data = process_learning_files(sentiment_files, 0, 5)
    return {
        'spam': spam_data,
        'sentiment': sentiment_data
    }

def classify_input(input, cls_data):
    input_vec = cls_data['vectorizer'].transform([input])
    X_train, X_test, y_train, y_test = train_test_split(cls_data['matrix'], cls_data['labels'], test_size=0.2, random_state=42)
    classifier = MultinomialNB(alpha=1.0)
    classifier.fit(X_train, y_train)
    input_as_matrix = np.array(input_vec)  # Convert sparse matrix to array
    probabilities = classifier.predict_proba(input_as_matrix.reshape(1, -1))
    predicted_label = classifier.predict([input_vec])[0]
    return predicted_label, probabilities


