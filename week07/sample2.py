# sample2.py
# This code will anonymise the sub domains of ip addresses
# Author: Fatima Zeino

import re

regex = "\d{1,3}\.\d{1,3} "
replacementText = "XXX.XXX "
filename="smallerAccess.log"
outputfilename="anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputfilename, 'w') as outputfile:
        for line in inputFile:
            newline = re.sub(regex, replacementText, line)
            outputfile.write(newline)