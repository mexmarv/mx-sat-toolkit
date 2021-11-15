# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

WORKDIR /app
CMD ["./serveapi.sh"]

