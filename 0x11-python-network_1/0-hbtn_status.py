#!/usr/bin/python3
""" Module designed for retrieving data from
'https://alx-intranet.hbtn.io/status' via HTTPS. """

import urllib.error
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print('Body response:')
            print(f'\t- type: {type(html)}')
            print(f'\t- content: {html}')
            print(f'\t- utf8 content: {html.decode("utf-8")}')
    except urllib.error.URLError as e:
        print(f"Error: {e}")
