#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -sX POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
