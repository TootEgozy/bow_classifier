import pytest
import asyncio

from index import classify_input, process_learning_data

from utils.get_text_by_label import get_texts_by_label


@pytest.fixture(scope="session")
async def setup_data():
    return await process_learning_data()

class TestClassifier:

    def test_classify_spam(setup_data):
        spam_texts = get_texts_by_label('spam', 5)

        for text in spam_texts:
            predicted_label = classify_input(text, 'spam', setup_data)
            print(predicted_label)
            assert predicted_label == 'spam'

    # def test_classify_ham(self):
    #     predicted_label, predictions_accuracy = classify_input('hi')
    #     print(predicted_label, predictions_accuracy)
    #     assert predicted_label == 'ham'
