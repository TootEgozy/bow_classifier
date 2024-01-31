import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


input = 'hello'
def process_learning_data(filepath):
    texts = list()
    labels = list()
    with open(filepath, 'r', encoding='latin1') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            labels.append(row[0].strip('"'))
            texts.append(row[1].strip('"'))
    vectorizer = CountVectorizer()
    X_bow = vectorizer.fit_transform(texts)
    return X_bow, labels, vectorizer

def input_to_vector(input, vectorizer):
    str_vec = vectorizer.transform([input])
    # print(str_vec.nonzero())
    return str_vec

[X_bow, labels, vectorizer] = process_learning_data('spam.csv')
input_vec = input_to_vector(input, vectorizer)

X_train, X_test, y_train, y_test = train_test_split(X_bow, labels, test_size=0.2, random_state=42)

spam_classifier = MultinomialNB()
spam_classifier.fit(X_train, y_train)

predictions = spam_classifier.score(X_test, y_test)
predicted_label = spam_classifier.predict(input_vec)

print("Predicted Label:", predicted_label[0])
print("Accuracy:", predictions * 100)
# learn how to add tests in python and write some tests


# TODO: polish the work and finish the flow
# connect frontend
# go live