#!/usr/bin/python3
""" Python script that fetches website"""


import urllib.request

if __name__ == '__main__':
    site = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(site) as response
    content = response.read()

    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
    print('\t- utf8 content: {}'.format(content.decode('utf-8')))
