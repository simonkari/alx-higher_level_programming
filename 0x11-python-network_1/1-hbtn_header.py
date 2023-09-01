#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request
from urllib.error import URLError

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except URLError as e:
        print(f"Error: {e}")
