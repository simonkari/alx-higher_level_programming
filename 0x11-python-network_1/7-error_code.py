#!/usr/bin/python3
"""Initiates a request to the provided URL and exhibits the content of the response body.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Send an HTTP GET request to the specified URL
    r = requests.get(url)

    # Check the status code of the response
    if r.status_code >= 400:
        # Handle HTTP errors by printing the error code
        print("Error code: {}".format(r.status_code))
    else:
        # Print the body of the response
        print(r.text)
