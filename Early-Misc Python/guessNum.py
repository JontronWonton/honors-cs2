# Jonathan Klein
# 9/18/18
# guessNum.py

# Create your own custom guessing game using for loops and while loops
# Be creative!

from random import *

num = randint(0,101)
guess = 0
running = True
count = 0

print("Can you guess my number?")

while running:
    guess = input("Please enter your guess\n")
    count = count + 1
    if guess == num:
        # If player guesses correctly
        print("\nWow you guessed my number!")
        print("It only took you " + str(count) + " guesses!")
        running = False
    elif guess > num:
        # If guess is too high
        print("\nToo high, buddy.")
    elif guess < num:
        # If guess is too low
        print("\nToo low, try again pal.")
