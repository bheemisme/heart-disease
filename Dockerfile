# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR .

# Copy the application code
COPY . .

# Install the dependencies
RUN pip3 install -r environment/requirements.txt

# Expose the port that the Flask app will use
EXPOSE 8080

# Run the command to start the Flask app
CMD ["python3", "./main.py"]
