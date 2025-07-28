# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (e.g., 8000 for FastAPI/Uvicorn, 80 for Flask/Gunicorn)
EXPOSE 8000

# Run the application with a WSGI server (e.g., Uvicorn for FastAPI, Gunicorn for Flask/Django)
# Adjust 'main:app' to match your actual application entry point
# Example for FastAPI:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Example for Flask (if 'app.py' has 'app = Flask(__name__)')
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]