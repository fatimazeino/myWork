# div.py
# This program reads in two numbers and 
# outputs the integer answer and remainder
# Author: Fatima Zeino

x = int(input("Enter First number: "))
y = int(input("Enter the number you want to divide by: "))
answer = x // y
remainder = x%y

print("{} divided by {} is {} with remainder {}".format(x,y,answer,remainder))