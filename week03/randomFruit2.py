# randomFruit2.py
# This program print out a random fruit
# Author : Fatima Zeino

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print ("A Random Fruit: {}".format(fruit))