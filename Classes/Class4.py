# Jonathan Klein
# 1/2/19
# Class4.py

"""
Create a card game!
User will receive two cards.  The combined value of the two cards will be compared to a random two cards (for a computer opponent).  Whoever has the highest combined value wins!

Part 1
- Create a Card class that includes lists of the standard cards
- For this game, Ace will only equal 11
- Face cards can equal 10 -OR- a number of your choice (below 13)
- You will need to determine the value of each card

Part 2
- Create a Hand class that will contain two Cards
- You will need to determine the value of your hand

Part 3
- Create a play() function that will display the users cards, an opponent’s (computer) cards and declare a winner


*BONUS
- Create a Player class
- Allow each Player to have a Hand with two cards
- Tally wins and losses
- Adapt the play() function to handle the Player class
"""

import random

class Card:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        pictureCards = ['Jack', 'Queen', 'King']
        numbers = range(1, 13)

        def __init__(self):
            self.suit = random.choice(Card.suits)
            self.number = random.choice(Card.numbers)
            self.face = self.number

        def determineType(self):
            if self.number == 1:
                self.face = 'Ace'
                self.number = 11
                return self.face
            elif self.number > 10:
                self.face = random.choice(Card.pictureCards)
                self.number = 10
                return self.face
            else:
                return self.face

class Hand:
    def __init__(self):
        self.card1 = Card()
        self.card2 = Card()

class Player:
    def __init__(self):
        self.score = 0

def play():
    # prints the cards
    print(f'You chose:\n{playerHand.card1.determineType()} of {playerHand.card1.suit}\n{playerHand.card2.determineType()} of {playerHand.card2.suit}\n')
    print(f'CPU chose:\n{cpuHand.card1.determineType()} of {cpuHand.card1.suit}\n{cpuHand.card2.determineType()} of {cpuHand.card2.suit}\n')

    # determines the higher pair of cards
    if playerHand.card1.number + playerHand.card2.number > cpuHand.card1.number + cpuHand.card2.number:
        print(f'You Win!!! ({playerHand.card1.number + playerHand.card2.number} vs {cpuHand.card1.number + cpuHand.card2.number})\n')
        player.score += 1
    elif playerHand.card1.number + playerHand.card2.number < cpuHand.card1.number + cpuHand.card2.number:
        print(f'You Lose! ({playerHand.card1.number + playerHand.card2.number} vs {cpuHand.card1.number + cpuHand.card2.number})\n')
        cpu.score += 1
    else:
        print(f'A draw! ({playerHand.card1.number + playerHand.card2.number} vs {cpuHand.card1.number + cpuHand.card2.number})\n')
        player.score += 1
        cpu.score += 1

rounds = 1
player = Player()
cpu = Player()

while True:
    playerHand = Hand()
    cpuHand = Hand()

    print('-'*50+'\n')
    print(f'ROUND {rounds}:\n')
    play()
    print(f'YOUR SCORE: {player.score}\nCPU SCORE: {cpu.score}\n')
    action = input('Would you like to play again? (Y/N)\n').lower()
    rounds += 1
    if action == 'n':
        print('-'*50+'\n')
        if player.score > cpu.score:
            print(f'You win!!!\n')
        elif player.score < cpu.score:
            print(f'You lose!\n')
        print(f'YOUR SCORE: {player.score}\nCPU SCORE: {cpu.score}\nROUNDS PLAYED: {rounds-1}')
        break

