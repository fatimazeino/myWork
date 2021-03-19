# normalise.py
# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case
# this program also outputs the length of the original string
# and the normalised one
# Author: Fatima Zeino

rawstring = input('Please enter a string: ')
normalisedstring = rawstring.strip().lower()

lenghtofrawstring = len(rawstring)
lenfhtofnormalisedstring = len(normalisedstring)
print('That string normalised is :{}'.format(normalisedstring))
print('we reduced the input string from {} to {} characters'.format(lenghtofrawstring,lenfhtofnormalisedstring))