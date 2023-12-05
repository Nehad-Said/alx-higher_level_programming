#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sX OPTIONS "$1" -I | sed -n 's/Allow: //p'
