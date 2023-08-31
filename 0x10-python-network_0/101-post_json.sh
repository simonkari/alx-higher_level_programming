#!/bin/bash
# The script sends a JSON POST request to a given URL with a given JSON file. is is passed as the first argument.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
