#!/usr/bin/python3
"""The script sends a POST request to http://0.0.0.0:5000/search_user with a letter.

Usage: ./8-json_api.py <letter>
  - letter sent as value of variable `q`.
  - No letter is provided, sends `q=""`.
"""

import requests
import sys

if __name__ == "__main__":
    # Determine the value of the 'letter' variable based on command-line arguments
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Create a dictionary 'payload' with the letter as the 'q' parameter
    payload = {"q": letter}

    # Send an HTTP POST request to the specified URL with the payload
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Attempt to parse the response as JSON
        response = r.json()

        if response == {}:
            print("No result")
        else:
            # Print the 'id' and 'name' fields from the JSON response
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # Handle cases where the response is not valid JSON
        print("Not a valid JSON")
