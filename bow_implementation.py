import nltk, re
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

normalizer = WordNetLemmatizer()

# get the most common pos for a word by counting it's occurrences in a dictionary
def get_pos(word):
    pos_counts = Counter({"n": 0, "v": 0, "a": 0, "r": 0})
    pos_options = wordnet.synsets(word)
    for item in pos_options:
        pos_counts[item.pos()] += 1
    return pos_counts.most_common(1)[0][0]

# clean, tokenize and normalize text to get a list of single words, edited based on their part-of-speech
def preprocess_text(text):
    cleaned = re.sub(r'\W+', ' ', text).lower()
    tokenized = word_tokenize(cleaned)
    normalized = [normalizer.lemmatize(token, get_pos(token)) for token in tokenized]
    return normalized

# convert a corpus into a bow object with words and their occurrences.
def create_bow(text):
    word_list = preprocess_text(text)
    bow = Counter(word_list)
    return bow

# create a dictionary from a bow
def create_dictionary(bow):
    dict = {}
    for i, word in enumerate(bow):
        dict[word] = i
    return dict

# create a bow from the new input, and a 0-full vector, then assign the word count to the vector.
# ignore new words. return the vector
def input_text_to_vector(input_text, dictionary):
    input_bow = create_bow(input_text)
    vector = [0] * len(dictionary)
    for word in input_bow:
        if word in dictionary:
            index = dictionary[word]
            vector[index] = input_bow[word]
    return vector

bow = create_bow('hello! I\'m happy to be using python and running my bow implementation')
dict = create_dictionary(bow)
input_text_to_vector('hello python!', dict)
