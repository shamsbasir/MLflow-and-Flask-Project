import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings

# Configure warnings to be logged explicitly
warnings.simplefilter("always")  # Log all warnings


def main():
    """
    Main function for training a Random Forest classifier and logging results with MLflow.
    """

    # Start an MLflow experiment
    mlflow.start_run()

    try:
        # Load the Iris dataset and split it into training and testing sets
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

        # Create and train a machine learning model (Random Forest)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions on the test data
        y_pred = model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)

        # Log parameters, metrics, and the trained model
        mlflow.log_params({"n_estimators": 100, "random_state": 42})
        mlflow.log_metrics({"accuracy": accuracy})

        # Save the model to MLflow
        mlflow.sklearn.log_model(model, "model")
    except Exception as e:
        # Log exceptions as errors
        mlflow.log_params({"error": str(e)})
    except Warning as warn:
        # Log warnings
        mlflow.log_params({"warning": str(warn)})
    finally:
        # End the MLflow run
        mlflow.end_run()







if __name__ == "__main__":
    main()
