#!/bin/bash

# Function to check if port is open
check_port() {
    local port=34170
    local ip="192.168.2.21"
    local max_attempts=30
    local attempt=1
    
    echo "Checking if port $port is open..."
    
    while [ $attempt -le $max_attempts ]; do
        if nc -z $ip $port; then
            echo "Port $port is open! Proceeding with Flask application startup..."
            return 0
        else
            echo "Attempt $attempt: Port $port is not open yet. Waiting..."
            sleep 2
            attempt=$((attempt + 1))
        fi
    done
    
    echo "Port $port did not open after $max_attempts attempts. Exiting..."
    return 1
}

# Check if netcat is installed
if ! command -v nc >/dev/null 2>&1; then
    echo "netcat is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y netcat
fi

# Run port check
if ! check_port; then
    exit 1
fi

# If port check succeeds, start the Flask application
cd /home/pi/dev/RPS
source venv/bin/activate
exec python3 play_main.py 