import sys
sys.path.append("..")
import pytest

from index import classify_input, process_learning_file

# TODO: add a better testing flow
# write a general function to sanitize data from files to provide the best learning data
# test individual functions and the flow using the sanitized data, try to get the prediction's accuracy in a range
cls_data = process_learning_file('../learning_data/sentiment.csv')

# class TestClassfier2:
#     # def test_classify_positive(self):
#     #     predicted_label, predictions_accuracy = classify_input('I\'m happy', cls_data)
#     #     print(predicted_label, predictions_accuracy)
#     #     assert predicted_label == '4'
#     #     # assert predictions_accuracy > 90
#     #
#     # def test_classify_negative(self):
#     #     predicted_label, predictions_accuracy = classify_input('this is so bad', cls_data)
#     #     print(predicted_label, predictions_accuracy)
#     #     assert predicted_label == '0'
#     #     # assert predictions_accuracy > 90
#
#     def test_testing(self):
#         assert 1+1==2

class TestClassfier2:
    @pytest.mark.test
    def test_testing(self):
        assert 1+1==2