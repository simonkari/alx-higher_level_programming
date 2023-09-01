#!/usr/bin/python3
"""Initiates a request to a provided URL and showcases the content of the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""

import urllib.error
import sys
import urllib.request

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Create a request object
    request = urllib.request.Request(url)

    try:
        # Send the request and get the response
        with urllib.request.urlopen(request) as response:
            # Print the response body
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the error code
        print("Error code: {}".format(e.code))
