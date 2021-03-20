# testLists.py
# This program reads on a list and prints it out item by item, and then prints it in reverse
# Author: Fatima Zeino

aList = [23, 'hi', True]

for item in aList:
    print(item)

print ('\n'.join(map(str,aList[::-1])))