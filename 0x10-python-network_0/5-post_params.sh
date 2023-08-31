#!/bin/bash
# Bash script for sending a POST request to a specified URL.
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
