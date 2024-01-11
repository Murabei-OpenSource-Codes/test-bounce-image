# Use a Python base image
FROM python:3.8-alpine

# Copy the current directory contents into the container
COPY app/ /app

# Install Flask
RUN pip install -r /app/requirements.txt

# Set the working directory in the container
WORKDIR /app

# Expose port 5000 for incoming HTTP requests
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
