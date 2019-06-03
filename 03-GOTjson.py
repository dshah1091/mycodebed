#!/usr/bin/python3

"""Author: DShah | Email: dshah1091@gmail.com | Learning GOTjson.py"""

# pull in json lib so we can parse out json
import json

def main():
    # open the jonsnow.json file in read model
    with open("jonsnow.json",'r') as gotdata:
        jonsnow = gotdata.read() 
        GOTpy = json.loads(jonsnow)
    print(GOTpy)
    print(GOTpy["url"])
    print(GOTpy["titles"][0])

    #create a loop to move across aliases
    with open("aliases.txt","w") as jsaliases:
        for gotalias in GOTpy["aliases"]:
            print(gotalias, file=jsaliases)
    
    print(GOTpy["aliases"]) #display values accoc. with aliases
    
if __name__ == "__main__":
    main()
