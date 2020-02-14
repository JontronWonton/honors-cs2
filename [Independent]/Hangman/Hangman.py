# Jonathan Klein
# 11/25/18
# Hangman.py (Edit)
# Original: https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman/

import time
from random import randint

wordList = open('Words.txt').read().split()
word = wordList[randint(0,len(wordList)-1)]
guesses = ''
wrongList = []
turns = 10

name = input('What is your name?\n')

print(f'Hey, {name}! Let\'s play hangman!\n')
time.sleep(0.5)

print('Loading...\n')
time.sleep(0.5)


while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1

    if failed == 0:
        print(f'\n\nYou won!')
        print(f'The word was "{word}"')
        print(f'You had {turns} misses remaining')
        break

    print(f'\nYou have {turns} misses remaining')

    if len(wrongList) != 0:
        print('You\'ve already tried: ' + ', '.join(map(str, wrongList)) + '\n')

    guess = input('Guess a character: ')
    guesses += guess
    time.sleep(0.25)

    print('=' * 50)

    if guess not in word:
        turns -= 1
        print('Incorrect!\n')
        wrongList.append(guess)
    else:
        print('Correct!\n')

    if turns == 0:
        print(f'You Lose!\nThe word was "{word}"')

