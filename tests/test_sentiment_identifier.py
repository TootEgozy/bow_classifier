import pytest

from index import classify_input, process_learning_data

from utils.get_text_by_label import get_texts_by_label


@pytest.fixture(scope="session")
def learning_data():
    return process_learning_data()


class TestSentimentClassifier:

    def test_classify_negative(self, learning_data):
        negative_inputs = get_texts_by_label('sentiment', '0', 5, 5,'sentiment_1.csv')
        print(negative_inputs)
        for input in negative_inputs:
            predicted_label = classify_input(input, 'sentiment', learning_data['sentiment'])
            assert predicted_label == '0'

    def test_classify_ham(self, learning_data):
        ham_inputs = get_texts_by_label('spam','ham', 10)
        for input in ham_inputs:
            predicted_label = classify_input(input, 'ham', learning_data['spam'])
            assert predicted_label == 'ham'
