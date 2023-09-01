#!/usr/bin/python3
"""Utilizes the GitHub API to retrieve a GitHub user ID
using the provided credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>

Employs Basic Authentication for accessing the user's ID.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
