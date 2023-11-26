# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Print the contents of requirements.txt for debugging
RUN cat requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Print the installed packages for debugging
RUN pip freeze

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=Crisko.settings

# Run migrations and start the Django development server
CMD ["bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]