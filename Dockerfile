# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8000"]
