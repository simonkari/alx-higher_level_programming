#!/usr/bin/python3
"""Dispatches a POST request to http://0.0.0.0:5000/search_user, specifying a particular letter.

Usage: ./8-json_api.py <letter>

The specified letter is sent as the value for the q variable.
If no letter is provided, it sends q="" as the query parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
