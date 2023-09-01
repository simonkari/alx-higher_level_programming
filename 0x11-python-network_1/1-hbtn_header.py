#!/usr/bin/python3
"""Retrieves the X-Request-Id header variable from a request made to a specified URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
