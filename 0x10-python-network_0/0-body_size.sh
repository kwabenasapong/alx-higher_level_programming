#!/bin/bash
# This script takes in a URL as its first argument and sends a request to that URL. It then displays the size of the body of the response in bytes.
curl -s "$1" | wc -c
