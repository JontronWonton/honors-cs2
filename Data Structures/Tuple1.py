# Jonathan Klein
# 11/2/18
# Tuple1.py


def line():
    print("-"*20)


def printObj(obj):
    for i in obj:
        print(i)


def tupleToList(tuple):
    resultList = []
    for i in tuple:
        resultList.append(i)
    return resultList


numTuple = (4, 3, 2, 1)
nameTuple = ('Jeremiah', 'Maurice', 'Humphrey', 'Adrian')

numList = [8, 7, 6, 5]
nameList = ['Bob', 'Gilbert', 'Christopher', 'Beter']

printObj(nameTuple)
line()

printObj(numTuple)
line()

print(nameTuple.index('Maurice'))
print(numList.index(6))
line()

print(30 in numTuple)
line()

print('Michael' in nameTuple)
line()

print(30 in numList)
line()

print('Michael' in nameList)
line()

printObj(reversed(nameTuple))
line()
printObj(reversed(numTuple))
line()
printObj(reversed(nameList))
line()
printObj(reversed(numList))
line()

printObj(sorted(nameTuple))
line()
printObj(sorted(numTuple))
line()
printObj(sorted(nameList))
line()
printObj(sorted(numList))
line()

myFavsTuple = ('Bob Saget', 'Bob Ross', 'Phil Swift', 'Papa John\'s', 'Billy Mays', 'Stefan Karl Stefansson')
printObj(myFavsTuple)
line()
printObj(reversed(myFavsTuple))
line()
printObj(sorted(myFavsTuple))
line()

tupleToList(myFavsTuple)
print(type((myFavsTuple)))
line()

printObj(myFavsTuple)
line()

for i in nameTuple:
    rev = reversed(i)
    for i in rev:
        print(i, end='')
    print('')
line()
