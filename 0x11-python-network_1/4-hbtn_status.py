#!/usr/bin/python3
"""Retrieves information from the URL "https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    # Send an HTTP GET request to the specified URL
    r = requests.get("https://alx-intranet.hbtn.io/status")

    # Print information about the response
    print("Body response:")
    # Print the type of the response content (usually str)
    print("\t- type: {}".format(type(r.text)))
    # Print the actual content of the response
    print("\t- content: {}".format(r.text))
