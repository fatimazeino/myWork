# grade.py
# This program reads in a students percentage mark and
# prints out corresponding the grade
# Author: Fatima Zeino

percentage = float(input("Enter the precentage: "))
if percentage < 0 or percentage > 100 :
    print ("Please enter a number between 0 and 100")
elif percentage < 40 :
    print("Fail")
elif percentage < 50 :
    print("Pass")
elif percentage < 60 :
    print("Merit01")
elif percentage < 70 :
    print("Merit02")
else:
    print("Distinction")