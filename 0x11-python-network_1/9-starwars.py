#!/usr/bin/python3
"""Dispatches a search query for a specified string to the Star Wars API.

Usage: ./9-starwars.py <search string>
  - The search request is sent to the Star Wars API search people endpoint.
"""
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./9-starwars.py <search string>")
        sys.exit(1)

    # Define the base URL for the Star Wars API
    url = "https://swapi.co/api/people"

    # Create a dictionary 'params' with the 'search' parameter
    params = {"search": sys.argv[1]}

    # Send an HTTP GET request to the specified URL with the 'search' parameter
    results = requests.get(url, params=params).json()

    # Print the number of results
    print("Number of results: {}".format(results.get("count")))

    # Print the names of matching characters
    [print(r.get("name")) for r in results.get("results")]
