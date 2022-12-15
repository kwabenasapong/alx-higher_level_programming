#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and displays the body of the response.
curl -s -X PUT 0.0.0.0:5000/catch_me -d "You got me!"
