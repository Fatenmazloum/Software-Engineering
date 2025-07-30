def test_sentiment_api_positive(client):
    response = client.post("/sentiment/predict-sentiment", json={"text": "I love programming!"})
    assert response.status_code == 200 #"OK, everything worked."
    data = response.json()#returns the response data as a Python dictionary
    assert data['sentiment'] == 'POSITIVE'#checks if the predicted sentiment is "POSITIVE" if not, the test fails 
    assert data['text'] == "I love programming!"


def test_sentiment_api_negative(client):
    response = client.post("/sentiment/predict-sentiment", json={"text": "I hate programming!"})
    assert response.status_code == 200 #"OK, everything worked."    
    data = response.json()#returns the response data as a Python dictionary
    assert data['sentiment'] == 'NEGATIVE'#checks if the predicted sentiment is "NEGATIVE" if not, the test fails
    assert data['text'] == "I hate programming!"

    #Sends a POST request to your API route /predict-sentiment.
    #Sends a JSON body: { "text": "I love it!" }
    # Checks that the API response was successful (HTTP 200 OK).
    # Checks that the response data includes a sentiment value and that it equals "POSITIVE".