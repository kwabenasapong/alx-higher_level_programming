#!/usr/bin/python3
'''
posting data to a server
'''

import urllib.request
import urllib.parse
import sys


def post_data():
    '''
    function to post data to a given url
    '''
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(data).encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        email_info = response.read('email').decode('utf-8')
    print(email_info)


if __name__ == "__main__":
    post_data()
