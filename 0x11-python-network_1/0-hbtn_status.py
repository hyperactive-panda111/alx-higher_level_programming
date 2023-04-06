#!/usr/bin/python3
""" Python script to fetch https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf-8 content: {}".format(body.decode('utf-8')))
