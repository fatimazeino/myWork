# average.py
# This program reads in numbers until
# the user enters 0
# it will them print b
# Author: Fatima Zeino

numbers = []
number = int(input("enter number (0 to quit): "))
while number != 0:
    numbers.append(number)
    number = int (input("enter another (0 to quit): "))
for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print ("the average is {}".format(average))
