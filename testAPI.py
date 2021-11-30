#!/usr/bin/env python3
""" Access APIs, Standard-Style"""

# standard library
import urllib.request
import json

URL="http://api.open-notify.org/iss-now.json"

def main():
    """pull JSON from an API and return it as Python"""

    resp=urllib.request.urlopen(URL)

    resp=resp.read()

    jsonstr=resp.decode("utf-8")
    final=json.loads(jsonstr)

    print(final)
    print(type(final))

main()
