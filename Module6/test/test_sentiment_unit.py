from app.services.sentiment_services import predict_sentiment
#should start with test_....

"""
You call the function with empty text (Step 2).

If the function gives an error (ValueError) because the input is empty, Python jumps to Step 4 and says:
"Good! The function did what it should do." → test passes (assert True)

BUT if the function does NOT give an error, Python goes to Step 3 and sees assert False → that means:
"This is bad! The function should have given an error, but it didn’t." → test fails
"""

def test_predict_sentiment():
    try:
        input_text = "" #1
        result=predict_sentiment(input_text)#2
        assert False, "Input text should not be empty"#3 test fails and shows ths message
    except ValueError as e:
        assert True#4 test passes

def test_positive_sentiment():
    input_text = "I love programming!"  # Example of positive sentiment
    result = predict_sentiment(input_text)
    assert result['label'] == 'POSITIVE', "Expected positive sentiment"

def test_negative_sentiment():
    input_text = "I hate programming!"  # Example of negative sentiment
    result = predict_sentiment(input_text)
    assert result['label'] == 'NEGATIVE', "Expected negative sentiment"

   
