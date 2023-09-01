#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id not found in the response headers.")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")
