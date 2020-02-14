# Jonathan Klein
# 12/21/18
# String Triangle.py

import pyperclip

inString = input('Give me a string and I\'ll apply the triangle effect.\n')
outString = ''


for i in range(len(inString)):
    outString += inString[:i] + '\n'

for j in range(len(inString), 0, -1):
    outString += inString[:j] + '\n'


print(outString)


while True:
    action = input('Would you like this copied to your clipboard? (Y/N)\n').lower()
    if action == 'y' or action == 'yes':
        pyperclip.copy(outString)
        print('Text successfully copied to your clipboard.\nHave a nice day. :)')
        break
    elif action == 'n' or action == 'no':
        print('Have a nice day. :)')
        break
    else:
        print('\nInvalid response.')
