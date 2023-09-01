#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import urllib.parse
import sys
import urllib.request

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    # Extract the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Create a POST request
    request = urllib.request.Request(url, data)

    try:
        # Send the request and get the response
        with urllib.request.urlopen(request) as response:
            # Print the body of the response
            print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        # Handle URL-related errors
        print(f"Error: {e.reason}")
        sys.exit(1)
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}")
        sys.exit(1)
