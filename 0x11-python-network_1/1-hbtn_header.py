#!/usr/bin/python3
"""
Retrieves the X-Request-Id header variable from a request made to a specified URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get("X-Request-Id")
            print(x_request_id)
    except urllib.error.URLError as e:
        print(f"Error: {e}")
