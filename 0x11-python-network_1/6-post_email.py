#!/usr/bin/python3
"""Initiates a POST request to the specified URL, including the provided email as part of the request data.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email data
    value = {"email": email}

    # Send an HTTP POST request to the specified URL with the email data
    r = requests.post(url, data=value)

    # Print the body of the response
    print(r.text)
