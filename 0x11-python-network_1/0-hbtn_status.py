#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html_doc = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html_doc)))
        print('\t- content: {}'.format(html_doc))
        print('\t- utf8 content: {}'.format(html_doc.decode('utf-8')))
