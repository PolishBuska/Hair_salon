# Use the Python 3.10 slim image based on Debian Bullseye
FROM python:3.10-slim-bullseye

# Label the maintainer
LABEL authors="stas"

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir --requirement requirements.txt

# Copy the rest of the application into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the app
CMD ["python3","run.py"]
