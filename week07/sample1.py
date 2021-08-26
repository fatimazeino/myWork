# sample1.py
# This is code will find some text in an access file
# Author: Fatima Zeino

import re

regex = "\[.*\]"
filename = "smallerAccess.log"

with open(filename) as inputFile:
    for line in inputFile:
      foundTextList = re.findall(regex, line)
      if (len(foundTextList)!= 0):
        #print(foundTextList)
        foundText = foundTextList[0]
        #print(foundText)
        # if I did not want the [] at the beginning and end
        print(foundText[1:-1])
