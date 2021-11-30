#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def get_stuff(url):
    resp = requests.get(url)
    return resp.json()

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        got_dj = get_stuff(AOIF_CHAR + got_charToLookup)

        print('Character: ' + got_dj['name'])

        for thingie in [('Houses:','allegiances'),('Books:','books'),('POV Books:','povBooks')]:
            print(thingie[0])
            if got_dj[thingie[1]]:
                for i in got_dj[thingie[1]]:
                    resp = get_stuff(i)
                    print('  ',resp['name'])
            else:
                print('   None')
            

if __name__ == "__main__":
        main()

