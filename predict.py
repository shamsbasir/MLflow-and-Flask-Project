import requests
import pandas as pd  # Import the pandas module

# URL of the Flask API endpoint
api_url = 'http://localhost:1000/predict'

# Input data in JSON format (replace with your data)
input_data = [
    [5.1, 3.5, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3]
]

# Send a POST request with input data
response = requests.post(api_url, json=input_data)

if response.status_code == 200:
    # Parse and print predictions
    response_json = response.json()
    if "predictions" in response_json:
        predictions = response_json["predictions"]
        print("Predictions:", predictions)
    else:
        print("Response does not contain 'predictions' key:", response_json)
else:
    print("Error:", response.text)
