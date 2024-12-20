# Use the official Python 3.10 image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY app.py /app/
COPY final_model.joblib /app/

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn joblib numpy scikit-learn pydantic

# Expose the port that the app will run on
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
