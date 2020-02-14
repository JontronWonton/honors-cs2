# Jonathan Klein
# 11/12/2018
# Dictionary1.py

def line():
    print("-"*50)


def printDict(dictionary):
    for key, value in dictionary.items():
        print("{}: {}".format(key, value))


def inDict(dictionary, search):
    for key, value in dictionary.items():
        if dictionary[key] == search:
            print('In dictionary')
            break
    else:
        print('Not in dictionary')

colorInt = {
    1 : 'Red',
    2 : 'Orange',
    3 : 'Yellow'
}

colorString = {
    'R' : 'Red',
    'O' : 'Orange',
    'Y' : 'Yellow'
}

for key, value in colorInt.items():
    print("{}: {}".format(key, value))
line()

print(colorInt[1])
print(colorString['Y'])
line()

print(len(colorInt))
print(len(colorString))
line()

colorInt[4] = 'Green'
colorInt[5] = 'Blue'
colorInt[6] = 'Purple'
colorInt[7] = 'Pink'
colorInt[8] = 'Brown'
printDict(colorInt)
line()

del colorInt[1]
printDict(colorInt)
line()

# BONUS BELOW

colorInt.update({8 : 'Black'})

inDict(colorInt, 'Purple')
line()

