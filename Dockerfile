# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /CyberHUB

# Copy the current directory contents into the container at /app
COPY . /CyberHUB

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the .env file into the container
COPY .env .env

# Set environment variables from .env file
ENV $(cat .env | xargs)

# Expose the port the app runs on
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]