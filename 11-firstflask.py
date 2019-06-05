#!/usr/bin/python3

from flask import Flask

app = Flask(__name__) # ALWAYS do this in your flask script

@app.route('/') #When you go to the ROOT of your server... do the following

def endoftheday(): #Function to trigger at ROOT
    return "Class is nearing the end for Wednesday" # RETURN this if you go to ROOT

if __name__ == "__main__":
    app.run(port=5006) #run on port 5006
