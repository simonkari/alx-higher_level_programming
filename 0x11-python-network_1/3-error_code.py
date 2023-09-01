#!/usr/bin/python3
"""Initiates a request to the provided URL and showcases
the content of the response body.

Usage: ./3-error_code.py <URL>

Manages HTTP errors during the process.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    # Check if the correct number of command-line arguments
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
