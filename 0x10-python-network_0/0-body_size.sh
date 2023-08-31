#!/bin/bash
# This script accepts a URL input, initiates a 
# request to the provided URL

curl -sI "$1" | grep Content-Length | cut -d " " -f2
