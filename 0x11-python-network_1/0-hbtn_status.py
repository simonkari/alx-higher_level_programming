#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body.decode('utf-8'))
except urllib.error.URLError as e:
    print("Error:", e)
