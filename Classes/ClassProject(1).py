# Jonathan Klein
# 1/8/19
# ClassProject.py

from random import *

class Contender:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.reloaded = True
        self.attacked = False
        self.protected = False
        self.blockLimit = 0
        self.turn = True
        self.printTurn = ''


    def select(self):
        while self.turn:
            action = str(input(f'\n{self.name}:\nWhat would you like to do?\nLoaded: {self.reloaded}\n\n(1) Attack\n(2) Block\n(3) Reload\n(4) Quit\n')).lower()
            newPage()
            if action == '1' or action == 'attack':
                if self.reloaded:
                    self.attack()
                    self.turn = False
                else:
                    print('Cannot attack unless reloaded!')
            elif action == '2' or action == 'block':
                if self.blockLimit == 2:
                    print('Cannot block more than twice in a row!\n')
                else:
                    self.block()
                    self.turn = False
            elif action == '3' or action == 'reload':
                if self.reloaded:
                    print('Already reloaded!\n')
                else:
                    self.reload()
                    self.turn = False
            elif action == '4' or action == 'quit':
                print('Have a nice day :)')
                quit()


    def attack(self):
        self.protected = False
        self.attacked = True
        self.reloaded = False
        self.blockLimit = 0
        self.printTurn = f'{self.name}: Attacked'


    def block(self):
        self.protected = True
        self.attacked = False
        self.blockLimit += 1
        self.printTurn = f'{self.name}: Blocked'


    def reload(self):
        self.reloaded = True
        self.protected = False
        self.attacked = False
        self.blockLimit = 0
        self.printTurn = f'{self.name}: Reloaded'


    @classmethod
    def printHealth(cls, p1, p2):
        print(f'{p1.name}: {p1.health} HP\n{p2.name}: {p2.health} HP')


    @classmethod
    def interpretation(cls, p1, p2):

        line()
        print(p1.printTurn, p2.printTurn, sep='\n')
        line()

        if p1.attacked and p2.attacked:
            # Checks if players attacked one another
            print(f'{p1.name} and {p2.name} attacked each other, inflicting 25 damage!\n')
            p1.health -= 25
            p2.health -= 25

        elif p1.attacked:
            # Checks if player attacked
            if p2.protected:
                print(f'{p1.name} attacked but {p2.name} blocked it!\n')
            else:
                print(f'{p1.name} attacked {p2.name} and dealt 25 damage!\n')
                p2.health -= 25

        elif p2.attacked:
            # Checks if CPU attacked
            if p1.protected:
                print(f'{p2.name} attacked but {p1.name} blocked it!\n')
            else:
                print(f'{p2.name} attacked {p1.name} and dealt 25 damage!\n')
                p1.health -= 25

        if not p1.attacked and not p2.attacked:
            print('A stalemate...\n')


def line():
    print('-'*50)


def newPage():
    print('\n'*50)


def main():
    rounds = 0
    # Keeps track of the amount of rounds played
    main = True

    print('-' * 50 + '\nWelcome to Duel!\nPlease select what you would like to do.\n(1) Player vs CPU\n(2) Player vs Player\n(3) Quit\n' + '-' * 50)
    while main:
        initAction = str(input()).lower()
        if initAction == '1':

            player1 = Contender('USER', 100, 25)
            cpu = Contender('CPU', 100, 25)
            # First generates two contenders for the duel (user and CPU)

            newPage()
            while True:
                player1.turn = True
                rounds += 1
                player1.select()
                # Above deals with player's turn only

                cpuAction = randint(1, 2)
                # Random value of 1 or 2 because there are only two possible options you can run at a time

                if cpu.reloaded:
                # First deduces whether the CPU can shoot or not
                    if cpu.blockLimit == 2 or cpuAction == 1:
                    # CPU must attack if they are beyond their block limit and they are reloaded
                    # Or if randint determines it
                        cpu.attack()
                    else:
                        cpu.block()
                else:
                    if cpu.blockLimit == 2 or cpuAction == 1:
                    # CPU must reload if they are beyond their block limit and they aren't reloaded
                    # Or if randint determines it
                        cpu.reload()
                    else:
                        cpu.block()
                # Above deals with CPU's turn only

                Contender.interpretation(player1, cpu)
                # Interprets the round
                Contender.printHealth(player1, cpu)
                # Prints player1 and cpu's health

                if player1.health == 0 and cpu.health == 0:
                    print(f'\nA draw! Better luck next time!\nROUNDS PLAYED: {rounds}')
                    break
                elif player1.health == 0:
                    # Checks if CPU won
                    print(f'\nYou lose!\nBetter luck next time!\nROUNDS PLAYED: {rounds}')
                    break
                elif cpu.health == 0:
                    # Checks if user won
                    print('''
                  _==___==_
                .-\:      /-.
               | (|:.     |) |
                '-|:.     |-'
                  \::.    /
                   '::. .'
                     ) (
                   _.'_'._
                  """""""""''')
                    print(f'\nYou win!!!\nROUNDS PLAYED: {rounds}')
                    break
                # Checks to see if anyone won the game
        elif initAction == '2':

            p1name = input('Player 1, enter your name: ')
            p2name = input('Player 2, enter your name: ')

            player1 = Contender(p1name, 100, 25)
            player2 = Contender(p2name, 100, 25)
            # First generates two contenders for the duel (two players)

            while True:
                rounds += 1

                player1.turn = True
                player1.select()
                # Above checks to see what player1 selected

                player2.turn = True
                player2.select()
                # Above checks to see what player2 selected

                Contender.interpretation(player1, player2)
                # Interprets what happened
                Contender.printHealth(player1, player2)
                # Prints the health of player1 and player2

                if player1.health == 0 and player2.health == 0:
                    print(f'\nA draw! Better luck next time!\nROUNDS PLAYED: {rounds}')
                    quit()
                elif player2.health == 0:
                    # Checks if player1 won
                    print('''
                   _==___==_
                 .-\:      /-.
                | (|:.     |) |
                 '-|:.     |-'
                   \::.    /
                    '::. .'
                      ) (
                    _.'_'._
                   """""""""''')
                    print(f'\n{player1.name} wins!\nROUNDS PLAYED: {rounds}')
                    quit()
                elif player1.health == 0:
                    # Checks if player2 won
                    print('''
                   _==___==_
                 .-\:      /-.
                | (|:.     |) |
                 '-|:.     |-'
                   \::.    /
                    '::. .'
                      ) (
                    _.'_'._
                   """""""""''')
                    print(f'\n{player2.name} wins!\nROUNDS PLAYED: {rounds}')
                    quit()
                # Checks to see if anyone won the game
        elif initAction == '3':
            print('Have a nice day :)')
            main = False
        else:
            print('Invalid input. Please try again.')


if __name__ == '__main__':
# Checks to see if program is being run or if classes are being exported into a separate file
    main()

