# This dockerfile runs the mabel-chat service as a production application. the run.py
# python file is where the service is started.
# which is the main file for the application

# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /app
ADD . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Run app.py when the container launches
CMD ["python", "run.py"]