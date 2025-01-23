#!/bin/bash

# Ensure a Python file is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

PYTHON_FILE=$1

# Check if the provided file exists
if [ ! -f "$PYTHON_FILE" ]; then
    echo "Error: File '$PYTHON_FILE' does not exist."
    exit 1
fi

# Store the initial checksum of the file
INITIAL_CHECKSUM=$(md5sum "$PYTHON_FILE")

# Function to start the Python file as a subprocess
start_python_file() {
    echo "Starting '$PYTHON_FILE'..."
    /home/sandeep/Projects/profile-site/venv/bin/python "$PYTHON_FILE" &
    PYTHON_PID=$!
}

# Function to stop the subprocess
stop_python_file() {
    if [ -n "$PYTHON_PID" ]; then
        echo "Stopping process (PID: $PYTHON_PID)..."
        kill "$PYTHON_PID"
        wait "$PYTHON_PID" 2>/dev/null
    fi
}

# Start the Python file initially
start_python_file

echo "Monitoring '$PYTHON_FILE' for changes. Press [Ctrl+C] to stop."

# Monitor the file for changes
while true; do
    # Calculate the current checksum
    CURRENT_CHECKSUM=$(md5sum "$PYTHON_FILE")

    # Check if the checksum has changed
    if [ "$INITIAL_CHECKSUM" != "$CURRENT_CHECKSUM" ]; then
        echo "Change detected in '$PYTHON_FILE'. Restarting..."
        stop_python_file
        start_python_file
        INITIAL_CHECKSUM=$CURRENT_CHECKSUM
    fi

    # Wait for 1 second before checking again
    sleep 1
done

# Clean up subprocess on exit
trap stop_python_file EXIT
