# Base image
FROM debian:12-slim

# Install VLC, Python and pip
RUN apt update && \
    apt install -y vlc python3 python3-pip && \
    apt clean

# Set working directory
WORKDIR /app

# Copy Python dependencies first (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Run the Flask app
CMD ["python3", "app.py"]
