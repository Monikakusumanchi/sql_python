# Use the official Python image as the base image
FROM python:3.9-alpine

# Install required system dependencies
RUN apk update && apk add --no-cache mariadb-connector-c-dev

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY app.py requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3306

# Run the Python script
CMD ["python", "app.py"]
