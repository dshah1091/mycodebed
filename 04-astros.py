#!/usr/bin/python3
  
""" Author: dshah1091@gmail.com | learning about API Requests"""


# Import Json
import json
#this allows the ability to import URLs
import urllib.request

# API is a constant so capitalize it:
MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    #make a Request
    resp = urllib.request.urlopen(MAJORTOM)

    #imake python strip json data from the resonse (it will be in a str format)
    jstring = resp.read()

    #convert the string data into json
    # print(jstring)
    # print(type(jstring))
    # print(dir(jstring))
    pyj = json.loads(jstring.decode('utf-8'))

    astrocosmo = pyj.get("people")

    for spaceperson in astrocosmo:
        print(spaceperson["name"])

if __name__ == "__main__":
    main()
    #parse out the Json we stripped off response
    #display selected data on screen - names of the people in space
