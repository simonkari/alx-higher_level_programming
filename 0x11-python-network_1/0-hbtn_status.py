#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    # Send an HTTP GET request to the URL and store the response in 'response'
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        # Read the content of the response (the HTML body) and store it in the 'html' variable
        html = response.read()
        
        # Display information about the response and its content
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
