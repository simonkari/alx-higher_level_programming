#!/bin/bash
# Obtain the size in bytes of the HTTP response header for a provided URL.

curl -s "$1" | wc -c
