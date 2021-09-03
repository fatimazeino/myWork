# jsondict.py
# This program that will store a simple Dict to a file as JSON
# Author: Fatima Zeino

import json
filename = "testdict.json"
sample = dict (name='fred', age= 31, grades=[1,34,55])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

# function that will read in a dict object from file
def readDict():
    with open(filename) as f:
        return json.load(f)

writeDict(sample)

somedict=readDict()
print(somedict)