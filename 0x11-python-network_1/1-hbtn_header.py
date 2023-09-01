#!/usr/bin/python3
"""Exhibits the X-Request-Id header variable from a
request made to the specified URL.

Usage: ./1-hbtn_header.py <URL>
"""

# Import the necessary libraries
import sys
import urllib.request

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Get the URL as a command-line argument
    url = sys.argv[1]

    # Create a urllib.request.
    request = urllib.request.Request(url)

    # Send an HTTP GET request and store the response in 'response'
    with urllib.request.urlopen(request) as response:
        # Extract the "X-Request-Id"
        print(dict(response.headers).get("X-Request-Id"))
