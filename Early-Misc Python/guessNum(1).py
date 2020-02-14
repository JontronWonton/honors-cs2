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
    guess = int(input("Please enter your guess\n"))
    count = count + 1
    if guess == num:
        print("\nWow well look at that aren't you smart.")
        print("It only took you " + str(count) + " guesses!")
        running = False
    elif guess > num:
        print("\nToo high, buddy.")
    else:
        print("\nToo low, try again pal.")
