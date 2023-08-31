#!/bin/bash
# Obtain the size in bytes of the HTTP response header for a provided URL.

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the provided URL and store the response in a variable
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the response body in bytes
echo "Size of the response body: $response bytes"
