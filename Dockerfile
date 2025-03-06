# Use a Python base image
FROM python:3.12.2

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
