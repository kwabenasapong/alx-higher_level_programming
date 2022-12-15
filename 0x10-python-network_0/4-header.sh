#!/bin/bash
# This script takes in a URL as its first argument and sends a GET request to that URL with a custom header. It then displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
