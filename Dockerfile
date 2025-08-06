# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables (adjust as needed)
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# Expose port if running a web server
EXPOSE 5000

# Run app (update based on your app's entry point, e.g., app.py or wsgi)
CMD ["python", "app.py"]
