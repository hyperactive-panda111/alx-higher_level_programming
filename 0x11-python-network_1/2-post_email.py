#!/usr/bin/python3
'''Sends POST request to email'''

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    site = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    request = urllib.request.Request(site, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
