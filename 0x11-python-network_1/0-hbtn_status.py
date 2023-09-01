#!/usr/bin/python3
"""
module that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
    
    print('Body response:')
    print(f'\t- type: {type(html)}')
    print(f'\t- content: {html}')
    print(f'\t- utf8 content: {html}')
