#!/usr/bin/python3
"""Author: dshah | Email: dshah1091@gmail.com | learning json with python"""

# with python, the jsonbatteries are in the box, but you need to plug them in
import json

def main():
    videogames =[{"game1": "red dead redemption", "game2": "witcher", "game3": "starcraft", "game4": "faster than light"},
            {"game1":"paperboy", "game2" : "donkey kong"}]

    #show the value of videogames
    print(videogames)

    # create a local file
    with open("videogames.json", "w") as vidfile: #'w' = write, 'r' = read, 'a' = append
        json.dump(videogames, vidfile)

if __name__ == "__main__":
    main()
