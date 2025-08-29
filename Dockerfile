# Use a Python 3.11 + Node.js 18 base image
FROM nikolaik/python-nodejs:python3.11-nodejs18

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Set working directory
WORKDIR /app/

# Install Python dependencies
RUN pip install --no-cache-dir -U -r requirements.txt

EXPOSE 8080

# Run the bot
CMD ["bash", "start"]
