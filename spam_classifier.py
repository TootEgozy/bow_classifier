# process explained:
# we get training data, convert it into a bow and then to a feature dictionary.
# each unique word in the dictionary is a column for the matrix.
# we decide on how to divide our data into documents. a document can be a word, a sentence, a row etc.
# each row in our matrix is the vectorised version of the document. 0's where words are not present and
# their count where they are.
# separate from that, we have our label's list. it's the length of our documents list length.
# now we have our data ready.
# we get a new input, and convert it to a vector: convert it into a BoW model, create an empty vector,
# and fill out the word count for each place in the vector (if the word is in our dictionary).
# MultinomialNB scans patterns in our matrix and finds the row which is most approximate to our vector.
# it returns the label from the labels list which matches the row in our matrix,
# and that's how our data gets classified.
# MultinomialNB can also give us it's accuracy estimation.

# convert the spam & ham file into a dictionary
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

# TODO: write the vectirization function for the new input
def input_to_vector(input, vectorizer):
    str_vec = vectorizer.transform([input])
    # print(str_vec.nonzero())
    return str_vec

[X_bow, labels, vectorizer] = process_learning_data('spam.csv')
# print(X_bow.shape)
input_vec = input_to_vector(input, vectorizer)

# add MultinomialNB and test a few inputs
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