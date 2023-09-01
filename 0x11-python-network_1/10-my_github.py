#!/usr/bin/python3
"""Utilizes the GitHub API to reveal a GitHub user ID based on provided authentication credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <GitHub username> <GitHub password>")
        sys.exit(1)

    # Create an authentication object using Basic Authentication
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # Send an HTTP GET request to the GitHub API for the authenticated user's information
    r = requests.get("https://api.github.com/user", auth=auth)

    # Parse the JSON response and print the user's ID
    print(r.json().get("id"))
