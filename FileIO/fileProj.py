# Jonathan Klein
# 2/6/19
# fileProj.py

# DUE 02/14/19
# Bank Project refactored

import datetime



time = datetime.datetime.now()
user = ''



class Account:

    accounts = {
                1: {
                    # This account is the admin account, only used for managing other Account.accounts
                    'Username' : 'Admin',
                    'Balance' : 0,
                    'PIN' : 1234567890,
                    'Admin' : True
                },
                2: {
                    'Username' : 'Henry',
                    'Balance' : 100,
                    'PIN' : 1234,
                    'Admin' : False
                },
                3: {
                    'Username' : 'James',
                    'Balance' : 100,
                    'PIN' : 5678,
                    'Admin' : False
                },
                4: {
                    'Username' : 'Keith',
                    'Balance' : 100,
                    'PIN' : 1357,
                    'Admin' : False
                },
                5: {
                    'Username' : 'Maurice',
                    'Balance' : 100,
                    'PIN' : 2468,
                    'Admin' : False
                }
            }

    accountPopulation = len(accounts)

    def __init__(self, name, balance, pin, admin, new=None):
        self.name = str(name)
        self.balance = int(balance)
        self.pin = str(pin)
        self.admin = admin
        if new:

            Account.accountPopulation += 1

            for i in Account.accounts:
                if Account.accounts[i]['Username'] == self.name:
                    print('ERROR\nUsername already in database.')
            else:
                Account.accounts[Account.accountPopulation] = {
                    'Username' : self.name,
                    'Balance' : self.balance,
                    'PIN' : self.pin,
                    'Admin' : self.admin
                }




    def deposit(self):
        global user
        while True:
            deposit = input('How much would you like to input?\nType "quit" to exit.\n')
            if deposit == 'quit':
            # if user tries to quit
                break
            elif 0 < int(deposit) <= 1000:
            # if deposit is in greater than 0 but equal to or less than 1000
                self.balance += int(deposit)
                # add the deposited amount to user's balance

                with open('Transactions.txt', 'a') as f:
                    f.write(f'[{time.now()}] {self.name}: Deposit of ${deposit}\n')

                # puts transaction on the user's log with current date
                print(f'Added ${str(deposit)} to your account.')
                break
            else:
                print('Invalid input. Please try again.\n')
    # adds money to user's account


    def withdraw(self):
        global user
        while True:
            withdraw = input('How much would you like to withdraw?\nType "quit" to exit.\n')
            if withdraw == 'quit':
            # if user tries to quit
                break
            elif int(withdraw) <= self.balance and int(withdraw) > 0:
            # if withdrawal is within sufficient funds
                self.balance -= int(withdraw)
                # subtracts withdrawal amount from user's balance

                with open('Transactions.txt', 'a') as f:
                    f.write(f'[{time.now()}] {self.name}: Withdrawal of ${withdraw}\n')

                # puts transaction on the user's log with current date
                print(f'Returned ${str(withdraw)} from your account.')
                break
            else:
                print('Insufficient funds. Please try again.\n')
    # removes money from user's account


    def checkBalance(self):
        global user
        print(f'Your balance is ${self.balance}.')
        with open('Transactions.txt', 'a') as f:
            f.write(f'[{time.now()}] {self.name}: Checked balance (${self.balance})\n')
    # checks the balance of a user's account


    def receipt(self):
        global user
        with open('Transactions.txt') as f:
            data = f.readlines()
            for line in data:
                print(line, end='')
        # prints the log, each separated by a new line
    # prints a log of all deposits and withdrawals done by a given user


    def addNewUser(self):

        if self.admin:
        # check for admin access first

            newUser = str(input('Enter new user\'s name\n'))
            newPIN = str(input('Enter new user\'s PIN\n'))
            newAdmin = str(input('Admin access? (True/False)\n'))

            tempString = str(Account.accountPopulation)
            vars()[tempString] = Account(newUser, 100, newPIN, newAdmin, new=True)

            # create new key in database with username and PIN of admin input
            # new user also gets a fresh log and balance of 100
            print(f'Successfully added new user "{newUser}" to database.\n')
    # adds a new user to database


    def printAllUsers(self):
        if self.admin:
        # check for admin access first
            for i in Account.accounts:
                print(f'{i}\nUsername: {Account.accounts[i]["Username"]}\nBalance: {Account.accounts[i]["Balance"]}\nPIN: {Account.accounts[i]["PIN"]}\nAdmin: {Account.accounts[i]["Admin"]}\n')
    # prints all users in database, along with each user's PIN and balance

def login():
    global user
    # reference of global variables
    loggedIn = False
    running = True
    while running:
    # keep repeating until condition is met
        pin = input('Please enter your PIN number.\nType "quit" to exit program.\n')
        if pin == 'quit':
            quit()
        Account.accounts.update()
        for i in Account.accounts:
            if int(pin) == Account.accounts[i]['PIN']:
            # if inputted PIN is equal to PIN in account database
                user = Account(Account.accounts[i]['Username'], Account.accounts[i]['Balance'], Account.accounts[i]['PIN'], Account.accounts[i]['Admin'])
                # store the found user in variable
                loggedIn = True
                print(f'Welcome, {user.name}.')
                running = False
                # break out of while loop
        if not loggedIn:
        # if PIN was never found in database, repeat loop
            print('Invalid PIN number. Please try again.\n')
# logs in to a user's account, proving admin access if necessary

def main():
    global user
    # access global variables
    print('\nWelcome to DankBank.')
    while True:
    # keep trying to login until a successful attempt
        login()
        while True:
            if user.admin:
            # access admin commands if admin access is available
                action = str(input('What would you like to do?\nOptions: "add user", "print all users", "logout"\n')).lower()
                # store user input inside variable 'action'
                if action == 'add user':
                # if user inputs 'add user'
                    user.addNewUser()
                elif action == 'print all users':
                # if user inputs 'print all users'
                    user.printAllUsers()
                elif action == 'logout':
                    user = ''
                    break
                else:
                # if user tries to excecute an unavailable action
                    print('Invalid action. Please try again.\n')
            else:
            # if user does not have admin access
                action = str(input('What would you like to do?\nOptions: "deposit", "withdraw", "check balance", "receipt", "logout"\n')).lower()
                # store user input inside variable 'action'
                if action == 'deposit':
                # if user inputs 'deposit'
                    user.deposit()
                elif action == 'withdraw':
                # if user inputs 'withdraw'
                    user.withdraw()
                elif action == 'check balance':
                # if user inputs 'check balance'
                    user.checkBalance()
                elif action == 'logout':
                # if user inputs 'logout'
                    user = ''
                    break
                elif action == 'receipt':
                # if user inputs 'receipt'
                    user.receipt()
                else:
                # if user tries to excecute an unavailable action
                    print('Invalid action. Please try again.\n')

if __name__ == '__main__':
    main()
# executes main bank app program
