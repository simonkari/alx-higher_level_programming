#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
