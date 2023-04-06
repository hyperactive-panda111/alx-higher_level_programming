#!/usr/bin/python3
''' Python script to fetch website'''
import requests

if __name__ == '__main__':
    site = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(site.text)))
    print('\t- content: {}'.format(site.text))
