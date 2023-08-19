# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir requests

# Make port 80 available to the world outside this container
# This is optional if you don't need network access from the container
EXPOSE 80

# Define environment variable
ENV NAME Puller

# Run puller.py when the container launches
CMD ["python", "puller.py"]
