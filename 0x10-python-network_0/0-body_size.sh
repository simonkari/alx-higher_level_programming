#!/bin/bash
# The script takes in a URL, then sends a request to that URL
curl -sI "$1" | grep Content-Length | cut -d " " -f2
