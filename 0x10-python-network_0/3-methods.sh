#!/bin/bash
# This script takes in a URL as its first argument and displays all HTTP methods that the server will accept.
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
