# topthree.py
# This program generates 10 random numbers.
# prints them out, then
# prints out the top 3
# I will use a list to store and
# manipulate the numbers
# Author: Fatima Zeino

import random
howmany = 10
topHowMany = 3
rangFrom = 0
rangeto = 100

numbers = []
for i in range(0,10) :
     numbers.append(random.randint(rangFrom,rangeto))
print ("{} random numbers \t {}".format(howmany, numbers))

topones = numbers.copy()
topones.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topones[0:topHowMany]))
