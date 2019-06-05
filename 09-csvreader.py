#!/usr/bin/python3

import csv

def main():
    with open('superbirths.csv') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader::
            print(row['heroname'], "is", row['name'])

if __name__ == "__main__":
    main()
