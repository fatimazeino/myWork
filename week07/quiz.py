# quiz.py
# this code for the quiz
# Author: Fatima Zeino

import re

regex = ".*"
filename= "quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingline = line
            print (matchingline, end="")