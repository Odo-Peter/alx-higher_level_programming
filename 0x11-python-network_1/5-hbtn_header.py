#!/usr/bin/python3
"""
Python script that sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == '__main__':
    body_res = requests.get(sys.argv[1])
    print(body_res.headers.get('X-Request-Id'))
