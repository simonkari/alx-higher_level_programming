#!/bin/bash
# This script takes in a URL, sends a request to that URL

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

content_length=$(curl -sI "$1" | awk -F': ' '/Content-Length/{print $2; exit}')

if [ -n "$content_length" ]; then
    echo "Content-Length: $content_length"
else
    echo "Content-Length header not found."
fi
