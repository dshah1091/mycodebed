#!/usr/bin/env python3
"""Author: Deep Shah | Email: dshah1091@gmail.com || learning json with python"""
#json is part of the standard library
import json

#json is part of the standard library
import json

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zapod Beeblerox",  "species" : "Betelgeusian"}, \
            {"name": "Arthur Dent", "species": "Human"}]

    ## display our python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    zfile = open("galaxyguide.json","w")

    ## use the json library
    ## USAGE: json.dump(input data, file like object) ##
    json.dump(hitchhikers, zfile)

    ##close the file when we are done
    zfile.close()

main()

