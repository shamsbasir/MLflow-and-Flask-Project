from flask import Flask, request, jsonify
import pandas as pd

import mlflow.pyfunc

# Load the model from MLflow
model_uri  = "runs:/06f7d6e0839945d79dbfe9948df53fb3/model" # Replace <RUN_ID> with the actual run ID

loaded_model = mlflow.pyfunc.load_model(model_uri)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        input_data = request.get_json()

        # Make predictions using the loaded model
        predictions = loaded_model.predict(pd.DataFrame(input_data))

        # Return predictions as JSON response
        return jsonify({"predictions": predictions.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)
