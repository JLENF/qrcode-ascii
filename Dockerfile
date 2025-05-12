FROM python:3.11-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Make sure the templates directory exists
RUN mkdir -p templates

# Create a non-root user to run the application
RUN useradd -m appuser
USER appuser

# Expose the port
EXPOSE 5001

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
