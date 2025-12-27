FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (optional - can be overridden by volume mount)
COPY . .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app:create_app
ENV FLASK_DEBUG=1

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

