# This dockerfile runs the run.py python file
# which is the main file for the application

# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /app
ADD . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run run.py when the container launches
CMD ["python", "run.py"]
