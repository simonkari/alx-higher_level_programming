#!/bin/bash
# Obtain the size in bytes of the HTTP response header for a provided URL.

curl -sI $1 | grep "Content-Length" | cut -d " " -f2
