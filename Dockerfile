# Use an official Python runtime as the base image
FROM python:3.9.7

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app

COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the MLflow model artifact into the container
COPY mlruns /app/mlruns

# Expose the port that Flask will run on
EXPOSE 1000

# Run the Flask application
CMD ["python", "app.py"]