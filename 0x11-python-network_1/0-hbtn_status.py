#!/usr/bin/python3
""" Module designed for retrieving data from 'https://alx-intranet.hbtn.io/status' via HTTPS. """
import urllib.request
import urllib.error


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as result:
        body = result.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".format(type(body), body, body.decode("utf-8")))
