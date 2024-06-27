# Use the official Python base image
FROM python:3.9.19-slim

# set the working directory in the container
WORKDIR /app

# copy requirements.txt in the container
COPY requirements.txt .

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code in the container
COPY . .

# set environment variables
ENV FLASK_APP=flask-orders-api
ENV FLASK_ENV=production

# expose the port the app runs on
EXPOSE 5000

# initialize the database
RUN flask init-db

# command to run the application
CMD [ "flask", "run", "--host=0.0.0.0"]
