#!/usr/bin/python3
""" Author: dshah1091@gmail.com | Near Earth Objects API"""

import requests
import pprint

MYAPI ="https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="

def keyharvester():
    with open("/home/student/nasa.key","r") as keyfile:
        mykey = keyfile.read()
        return mykey.rstrip('\n')

def main():
    # harvest our key from /home/student/nasa.key
    nasakey = keyharvester()

    #print(MYAPI + nasakey)
    # append our key to the myapi
    # Call the API # and pull off json (.json())
    asteroidz = requests.get(MYAPI + nasakey).json()

    #print(asteroidz)
    # Parse json - loop across "near_earth_objects" to reveal astroids

    #pprint.pprint(asteroidz["near_earth_objects"])
    for bigrock in asteroidz["near_earth_objects"]:
        if bigrock.get("is_potentially_hazardous_asteroid"): 
            print(bigrock['name'])

        print()
    # only destroy those thay may pose a danger to Deep having a good weekend
if __name__ == "__main__":
    main()

