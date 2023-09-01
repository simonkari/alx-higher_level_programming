#!/usr/bin/python3
""" This is a Python script that retrieves information 
from the URL "https://alx-intranet.hbtn.io/status
"""
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as result:
        body = result.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".format(type(body), body, body.decode("utf-8")))