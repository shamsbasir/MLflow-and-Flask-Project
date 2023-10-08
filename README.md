# MLflow and Flask Project

This repository showcases the integration of MLflow for model training and logging, Flask for deploying a web service, and making predictions using the trained model.

## Getting Started

Follow these steps to get started with the project:

### Prerequisites

Ensure that you have the following prerequisites installed:

- Python 3.x
- [MLflow](https://mlflow.org/) (You can install it using `pip install mlflow`)
- [Flask](https://flask.palletsprojects.com/) (You can install it using `pip install Flask`)
- [Requests](https://pypi.org/project/requests/) (You can install it using `pip install requests`)

### Project Structure

Here's an overview of the project structure:

```
my_project/
│
├── main.py
├── app.py
├── predict.py
├── requirements.txt
├── README.md
```

- `main.py`: This script is responsible for training a Random Forest classifier and logging the results with MLflow.
- `app.py`: Sets up a Flask web service for making predictions.
- `predict.py`: Sends a POST request to the Flask API to generate predictions.
- `requirements.txt`: Lists project dependencies.
- `README.md`: This document provides an overview of the project and usage instructions.

## Training the Model

To train the Random Forest classifier and log the results with MLflow, follow these steps:

1. Open your terminal.
2. Navigate to the project directory.
3. Run the following command:

```bash
python main.py
```

This script will initiate an MLflow run and store the trained model.

## Deploying the Flask App

To deploy the Flask application for making predictions, follow these steps:

1. Open another terminal.
2. Navigate to the project directory.
3. Run the following command:

```bash
python app.py
```

The Flask app will be hosted at `http://localhost:8000`.

## Making Predictions

To make predictions using the deployed model, follow these steps:

1. Open yet another terminal.
2. Navigate to the project directory.
3. Run the following command:

```bash
python predict.py
```

This script will send a POST request to the Flask API and display the predictions.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.