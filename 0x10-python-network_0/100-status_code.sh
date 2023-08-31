#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -s -o "$response_file" -w "%{http_code}" "$1"
