#!/usr/bin/python3
"""Dispatches a POST request to http://0.0.0.0:5000/search_user,
specifying a particular letter.

Usage: ./8-json_api.py <letter>

The specified letter is sent as the value for the q variable.
If no letter is provided, it sends q="" as the query parameter.
"""
# Import the necessary libraries
import sys
import requests

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Initialize an empty string 'letter'
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Create a dictionary 'payload' with a single key "q"
    payload = {"q": letter}

    # Send an HTTP POST request to a local server
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    # Try to parse the response as JSON
    try:
        response = r.json()

        # Check if the response is an empty dictionary
        if response == {}:
            print("No result")
        else:
            # Print the "id" and "name" fields from the response
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # Handle the case where the response is not valid JSON
        print("Not a valid JSON")
