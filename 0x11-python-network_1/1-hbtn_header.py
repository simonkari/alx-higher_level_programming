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
    # Get the URL as a command-line argument (assuming it's the first argument)
    url = sys.argv[1]

    # Create a urllib.request.Request object for the specified URL
    request = urllib.request.Request(url)

    # Send an HTTP GET request to the URL and store the response in 'response'
    with urllib.request.urlopen(request) as response:
        # Extract the "X-Request-Id" header from the response's headers and print it
        print(dict(response.headers).get("X-Request-Id"))
