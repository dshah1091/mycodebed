#!/usr/bin/python3

import csv
import json

def main():
    # open a file to dump Json to
    jsonf = open('superbirths.json','w')
    
    # open our CSV file to read in CSV to python format
    with open('superbirths.csv') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            json.dump(list(reader), jsonf)
    jsonf.close() #close the superbirth.json file we opened

if __name__ == "__main__":
    main()
