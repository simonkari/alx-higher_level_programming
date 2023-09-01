#!/usr/bin/python3
""" Module that fetches https://intranet.hbtn.io/status """
import urllib.request as request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    
    with request.urlopen(url) as response:
        body = response.read().decode("utf-8")
    
    print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body}")
