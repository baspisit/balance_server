# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Expose the port your server listens on (if applicable)
EXPOSE 65432

# # Install any needed packages specified in requirements.txt
RUN pip install numpy

# Copy the rest of your application's code into the container
COPY . .

# Specify the command to run your application
CMD [ "python", "server.py" ]

