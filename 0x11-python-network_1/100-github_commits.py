#!/usr/bin/python3
"""Enumerates the ten most recent commits in a specified GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
# Import the necessary libraries
import requests
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Build the URL for GitHub API using command-line arguments
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Send an HTTP GET request to the constructed URL
    r = requests.get(url)

    # Parse the JSON response from the API into a list of commits
    commits = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        # Handle the case where there are fewer than 10 commits
        pass
