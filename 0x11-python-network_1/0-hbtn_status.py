#!/usr/bin/python3
<<<<<<< HEAD
""" Python script that fetches website"""


=======
''' Python script that fetches website'''
>>>>>>> 6155015af227d8a0f35ab61bbd5e30e4546e49d4
import urllib.request

if __name__ == '__main__':
    site = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(site) as response
    content = response.read()

    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
    print('\t- utf8 content: {}'.format(content.decode('utf-8')))
