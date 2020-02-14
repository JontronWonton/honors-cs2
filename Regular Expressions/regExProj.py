# Jonathan Klein
# 4/15/19
# regExProj.py

from regEx1 import regExChecker, line

class Account(object):
    list = []
    def __init__(self, username, password, email, pn):
        self.username = username
        self.password = password
        self.email = email
        self.pn = pn

input('Hello, welcome to the account creator!\nPress ENTER to proceed.\n')

usernameBool = True
while usernameBool:
    line(' USERNAME ')
    username = input('Please enter a valid username.\n- Must be between 3 and 16 letters in length\n- Must only use letters and numbers with the exception of underscores\n')
    if regExChecker(username, '^\w{3,16}$'):
        usernameBool = False
    else:
        print('\nINVALID USERNAME')

passwordBool = True
while passwordBool:
    line(' PASSWORD ')
    password = input('Please enter a valid password.\n- Must be between 6 and 16 characters in length\n- Must contain at least one capital letter\n- Must contain at least 1 number\n')
    if regExChecker(password, '((?=(.*[0-9]))(?=(.*[A-Z])))^.{6,16}$'):
        passwordBool = False
    else:
        print('\nINVALID PASSWORD')

emailBool = True
while emailBool:
    line(' EMAIL ')
    email = input('Please enter a valid email.\n- Must be a valid email\n\t- Contain an @ symbol\n\t- Contain a valid domain (such as gmail.com)\n')
    if regExChecker(email, '(^[\w\d-]+@[a-z\d-]+\.[a-z]{2,3}$)'):
        emailBool = False
    else:
        print('\nINVALID EMAIL')

pnBool = True
while pnBool:
    line(' PHONE NUMBER ')
    pn = input('Please enter a valid phone number.\n- Enter in the form 555-555-5555\n')
    if regExChecker(pn, '^[\d]{3}-[\d]{3}-[\d]{4}$'):
        pnBool = False
    else:
        print('\nINVALID PHONE NUMBER')

Account.list.append(Account(username, password, email, pn))
line(' ACCOUNT CREATED ')
