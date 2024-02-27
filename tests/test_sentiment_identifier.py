import pytest

from index import classify_input, process_learning_data

from utils.get_text_by_label import get_texts_by_label


@pytest.fixture(scope="session")
def learning_data():
    return process_learning_data()

# These tests are unstable. some labels in the csv files are wrong (good training data is hard to come by)
# and the model classifies the texts correctly, so the test fails
class TestSentimentClassifier:

    def test_classify_negative(self, learning_data):
        negative_inputs = get_texts_by_label('sentiment', '0', 5, 5,'sentiment_1.csv') + \
                          get_texts_by_label('sentiment', '0', 5, 5,'sentiment_2.csv')
        for input in negative_inputs:
            predicted_label = classify_input(input, 'sentiment', learning_data['sentiment'])
            assert predicted_label == 'negative', f"Assertion failed for input = {input}"

    def test_classify_positive(self, learning_data):
        positive_inputs = get_texts_by_label('sentiment', '4', 5, 5,'sentiment_4.csv') + \
                          get_texts_by_label('sentiment', '4', 5, 5,'sentiment_5.csv')
        for input in positive_inputs:
            predicted_label = classify_input(input, 'sentiment', learning_data['sentiment'])
            assert predicted_label == 'positive', f"Assertion failed for input = {input}"
