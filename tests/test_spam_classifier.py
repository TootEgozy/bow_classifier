from index import classify_input

# TODO: add a better testing flow
# write a general function to sanitize data from files to provide the best learning data
# test individual functions and the flow using the sanitized data, try to get the prediction's accuracy in a range

class TestClassfier:

    def test_classify_spam(self):
        predicted_label, predictions_accuracy = classify_input('FREE')
        print(predicted_label, predictions_accuracy)
        assert predicted_label == 'spam'
        assert predictions_accuracy > 90

    def test_classify_not_spam(self):
        predicted_label, predictions_accuracy = classify_input('hi')
        print(predicted_label, predictions_accuracy)
        assert predicted_label == 'ham'
        assert predictions_accuracy > 90
