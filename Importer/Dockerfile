# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the Importer script to the container
COPY importer.py /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir pandas pymongo

# Run the Importer script when the container launches
CMD ["python", "importer.py"]
