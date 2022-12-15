#!/bin/bash
# This script takes in a URL as its first argument and sends a DELETE request to that URL. It then displays the body of the response.
curl -sX DELETE "$1"
