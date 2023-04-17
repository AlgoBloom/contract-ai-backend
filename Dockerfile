# Use an official Python runtime as a parent image
FROM python:3.9.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to use Mythril in the CLI
ENV MYTHRIL_CLI_ARGS --verbose --solv 0.8.4

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME Mythril Audit

# Run app.py when the container launches
CMD ["gunicorn", "app:app-20", "--log-file=-"]
