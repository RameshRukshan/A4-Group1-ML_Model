# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install virtualenv && \
    python -m virtualenv venv && \
    /bin/bash -c "source venv/bin/activate" && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install Flask==3.0.0

# Make port 3300 available to the world outside this container
EXPOSE 3300

# Run app.py when the container launches
CMD ["python", "app.py"]
