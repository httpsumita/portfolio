# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set environment variables to optimize Python's behavior in the container
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for Pillow and other packages
RUN apt-get update && apt-get install -y \
    libjpeg-dev zlib1g-dev libpng-dev libwebp-dev build-essential \
    && apt-get clean

# Copy requirements file to the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Ensure static files are collected
RUN python manage.py collectstatic --noinput

# Expose the port Django's development server will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]