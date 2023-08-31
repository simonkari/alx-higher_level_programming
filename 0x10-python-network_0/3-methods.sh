#!/bin/bash
# Show the complete list of HTTP methods that the server for a provided URL is willing to accept.
curl -s -I -X OPTIONS "$1"
