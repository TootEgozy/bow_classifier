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


def create_dictionary(filepath):
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
    print(X_bow.shape)

create_dictionary('spam.csv')

# TODO: write the vectirization function for the new input
# add MultinomialNB and test a few inputs
# learn how to add tests in python and write some tests

# TODO: poish the work and finish the flow
# connect frontend
# go live