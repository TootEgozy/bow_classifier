import pytest

from index import classify_input, process_learning_data

from utils.get_text_by_label import get_texts_by_label


@pytest.fixture(scope="session")
def learning_data():
    return process_learning_data()


class TestClassifier:

    def test_classify_spam(self, learning_data):
        spam_inputs = get_texts_by_label('spam', 'spam', 10)
        for input in spam_inputs:
            predicted_label = classify_input(input, 'spam', learning_data['spam'])
            assert predicted_label == 'spam'

    def test_classify_ham(self, learning_data):
        ham_inputs = get_texts_by_label('spam','ham', 10)
        for input in ham_inputs:
            predicted_label = classify_input(input, 'ham', learning_data['spam'])
            assert predicted_label == 'ham'
