#!/usr/bin/python3
  
""" Author: dshah1091@gmail.com | learning about API Requests"""

#using the requests library
import requests

# API is a constant so capitalize it:
MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    try: #make a Request
        pyj = (requests.get(MAJORTOM)).json()

        astrocosmo = pyj.get("people")

        for spaceperson in astrocosmo:
            print(spaceperson["name"])
    except:
        print("API is unavailable at the moment")
        exit()

if __name__ == "__main__":
    main()
    #parse out the Json we stripped off response
    #display selected data on screen - names of the people in space
