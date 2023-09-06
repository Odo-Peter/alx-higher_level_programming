#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    query = sys.argv[1] if len(sys.argv) >= 2 else ""
    res = requests.post(url, data={'q': query})
    try:
        res_dict = res.json()
        if res_dict:
            print("[{}] {}".format(res_dict.get('id'), res_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
