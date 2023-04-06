#!/usr/bin/python3
''' Displays the X-Request-Id header'''

import sys
import requests

if __name__ == "__main__":
    site = sys.argv[1]
    req = requests.get(site)
    print(req.headers.get('X-Request-Id'))
