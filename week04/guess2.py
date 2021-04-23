# guess2.py
# This program prompts the user to guess a number
# the program keeps prompting the user to guess the number
# the program tells the user if there guess is too high or too low, each time they guess
# until the user gets the right on
# Author: Fatima Zeino

#numberToGuess = 30

import random
randomNumber = random.randint(0,100)

guess = int (input("Please guess the number: "))
while guess != randomNumber:
    if guess < randomNumber:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", randomNumber)