#!/usr/bin/env python3

""" Accessing APIs, 3rd Party Style"""

import requests

URL="http://api.open-notify.org/iss-now.json"

def main():
    resp=requests.get(URL)

    final=resp.json()

    print(final)

main()
