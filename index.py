import csv
import os
import random

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

from utils.get_text_by_label import get_texts_by_label
from utils.get_data_path import get_data_path


def process_learning_files(cls_type, label_index, text_index):
    learning_data_path = get_data_path(cls_type)
    filenames = os.listdir(learning_data_path)
    texts = list()
    labels = list()
    for filename in filenames:
        with open(f'{learning_data_path}/{filename}', 'r', encoding='latin1') as file:
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
    spam_data = process_learning_files('spam', 0, 1)
    sentiment_data = process_learning_files('sentiment', 0, 5)
    return {
        'spam': spam_data,
        'sentiment': sentiment_data
    }

def label_to_text(cls_type, predicted_label):
    if(cls_type == 'sentiment'):
        match predicted_label:
            case '0':
                return 'negative'
            case '2':
                return 'neutral'
            case '4':
                return 'positive'
    else:
        return predicted_label

def classify_input(input, cls_type, cls_data):
    input_vec = cls_data['vectorizer'].transform([input])
    X_train, X_test, y_train, y_test = train_test_split(cls_data['matrix'], cls_data['labels'], test_size=0.2, random_state=42)
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)
    predicted_label = classifier.predict(input_vec)[0]
    return label_to_text(cls_type, predicted_label)

def round_up_to_even(n):
    return n + 1 if n % 2 != 0 else n

def get_inputs_for_user(cls_type, count):
    half_count = int(round_up_to_even(count) / 2)
    inputs = []
    match cls_type:
        case 'spam':
            inputs = get_texts_by_label(cls_type, 'spam', half_count, 1) + \
                get_texts_by_label(cls_type, 'ham', half_count, 1)
        case 'sentiment':
            inputs = get_texts_by_label(cls_type, '0', half_count, 5, 'sentiment_1.csv') + \
                     get_texts_by_label(cls_type, '4', half_count, 5, 'sentiment_4.csv')
    return(random.sample(inputs, count))