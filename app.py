# Import necessary libraries
from flask import Flask, request, jsonify  # Import Flask for web app, request for HTTP handling, and jsonify for JSON responses
import pandas as pd  # Import pandas for data manipulation
import mlflow.pyfunc  # Import mlflow.pyfunc for loading MLflow models

# Import necessary libraries
import mlflow

# Get the MLflow tracking URI
mlflow_tracking_uri = mlflow.get_tracking_uri()

# Use the tracking URI to build the model URI
latest_run = mlflow.search_runs(order_by=["start_time desc"]).iloc[0]
model_uri = f"{mlflow_tracking_uri}/0/{latest_run.run_id}/artifacts/model"

# Load the MLflow model using mlflow.pyfunc.load_model()
loaded_model = mlflow.pyfunc.load_model(model_uri)

# Now you can use `loaded_model` to make predictions or perform other operations with the loaded model.

app = Flask(__name__)  # Initialize a Flask application

# Define a route and function for making predictions
@app.route('/predict', methods=['POST'])  # Define a route '/predict' that accepts HTTP POST requests
def predict():
    try:
        # Get input data from the request
        input_data = request.get_json()  # Extract JSON data from the HTTP request

        # Make predictions using the loaded model
        predictions = loaded_model.predict(pd.DataFrame(input_data))  # Use the model to make predictions on input data

        # Return predictions as a JSON response
        return jsonify({"predictions": predictions.tolist()})  # Convert predictions to a JSON response
    
    except Exception as e:
        # Handle exceptions (e.g., invalid input or model errors) and return an error message as a JSON response
        return jsonify({"error": str(e)})  # Convert the exception message to a JSON response

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)  # Start the Flask development server on host '0.0.0.0' and port 1000
