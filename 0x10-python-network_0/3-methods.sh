#!/bin/bash
# Show the complete list of HTTP methods that the server for a provided URL is willing to accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
