# tests/test_app.py
from app.app import app

import json

# Test for the home (index) route
def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data  # Update based on actual content in index.html

# Test for the prediction endpoint
def test_predict_route():
    # Use sample input text for prediction
    sample_data = {"text": "I love this product!"}
    
    # Send POST request to /predict endpoint
    response = app.test_client().post(
        '/predict',
        data=json.dumps(sample_data),
        content_type='application/json'
    )
    
    # Assert the response status code and prediction content
    assert response.status_code == 200
    data = response.get_json()
    assert "label" in data and data["label"] in ["Positive", "Negative"]
