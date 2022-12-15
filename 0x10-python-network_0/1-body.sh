#!/bin/bash
# This script takes in a URL as its first argument and sends a GET request to that URL. It then displays the body of the response if the response has a 200 status code.
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -sL "$1"
