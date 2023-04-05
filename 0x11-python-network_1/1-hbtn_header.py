#!/usr/bin/python3
''' Python script that takes in a URL, sends a request and displays value'''
import urllib.request
import sys

if __name__ == '__main__':
    url =sys.argv[1]
    url_request = urllib.request.Request(url)
    with urllib.response.request.urlopen(url_request) as response:
        print(dict(response.headers).get('X-Request-Id'))
