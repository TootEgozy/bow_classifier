from spam_classifier import classify_spam

def test_classify_spam():
    predicted_label, predictions_accuracy = classify_spam('FREE')
    assert predicted_label == 'spam'
    assert predictions_accuracy > 90
