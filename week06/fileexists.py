# fileexists.py
# This program that checks if the file exists
# Author: Fatima Zeino


import os.path

filename = "count.txt"
if not os.path.isfile(filename):
    print("File does not exist")
    # initialise file here
    writeNumber(0)

def readNumber():
    try:
        with open(filename) as f:
            number=int(f.read())
            return number
    except IOError:
        return 0