#!/usr/bin/python3
''' Sends request to a given URL and displays the response body'''

import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    site = sys.argv[1]
    request = urllib.request.Request(site)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('ascii')
    except urlib.error.HTTPError as x:
            print("Error code: {}".format(x.code))
