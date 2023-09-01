#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request

# URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Send an HTTP GET request to the URL and store the response in 'response'
with urllib.request.urlopen(url) as response:
    # Read the content of the response (the HTML body) and store it in the 'html' variable
    html = response.read().decode('utf-8')

    # Display the body of the response with proper tabulation
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
