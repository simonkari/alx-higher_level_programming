#!/usr/bin/python3
"""Shows the X-Request-Id header value from a request sent to a specified URL.

Usage: ./5-hbtn_header.py <URL>
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Send an HTTP GET request to the specified URL
    r = requests.get(url)

    # Check if the "X-Request-Id" header exists in the response
    x_request_id = r.headers.get("X-Request-Id")
    if x_request_id is not None:

        print(x_request_id)
