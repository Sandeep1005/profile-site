#!/bin/bash

# Ensure a directory is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

DIRECTORY=$1

# Check if the provided directory exists
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: Directory '$DIRECTORY' does not exist."
    exit 1
fi

# Function to calculate checksum for all .py files in the directory
calculate_checksum() {
    find "$DIRECTORY" -type f -name "*.py" -exec md5sum {} \; | sort | md5sum
}

# Function to start the Python subprocess
start_python_service() {
    echo "Starting Python service..."
    venv/bin/python app.py &  # Replace 'main.py' with your entry point script
    PYTHON_PID=$!
}

# Function to stop the Python subprocess
stop_python_service() {
    if [ -n "$PYTHON_PID" ]; then
        echo "Stopping process (PID: $PYTHON_PID)..."
        kill "$PYTHON_PID"
        wait "$PYTHON_PID" 2>/dev/null
    fi
}

# Initial checksum
INITIAL_CHECKSUM=$(calculate_checksum)

# Start the Python subprocess
start_python_service

echo "Monitoring '.py' files in '$DIRECTORY' for changes. Press [Ctrl+C] to stop."

# Monitor for changes
while true; do
    CURRENT_CHECKSUM=$(calculate_checksum)

    if [ "$INITIAL_CHECKSUM" != "$CURRENT_CHECKSUM" ]; then
        echo "Change detected in '.py' files. Restarting..."
        stop_python_service
        start_python_service
        INITIAL_CHECKSUM=$CURRENT_CHECKSUM
    fi

    sleep 1
done

# Cleanup subprocess on script exit
trap stop_python_service EXIT
