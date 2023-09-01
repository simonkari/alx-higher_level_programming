#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """

# Import the necessary library
import urllib.request

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Send an HTTP GET request and store the response in 'response'
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        # Read the content of the response and store it in the 'html' variable
        html = response.read()

        # Print information about the response and its content
        print('Body response:')
        # Print the type of the response content
        print('\t- type: {}'.format(type(html)))
        # Print the raw content (bytes) 
        print('\t- content: {}'.format(html))
        
        # Decode the content from bytes to UTF-8 and print it
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
