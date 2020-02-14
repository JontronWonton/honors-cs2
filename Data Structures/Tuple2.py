# Jonathan Klein
# 11/6/18
# Tuple2.py

myTuple = ('Arizona', 'Connecticut', 'Kansas', 'New Jersey', 'Wyoming')


def line():
    print("\n"+"-"*50)


def printObj(tup):
    for i in tup:
        print(i, end=' ')


def tupleRemoveLast(tup, item):
    resultList = []
    for i in tup:
        resultList.append(i)
    resultList.remove(item)
    newTuple = tuple(resultList)
    return newTuple

printObj(myTuple)
line()

myTuple = tupleRemoveLast(myTuple, 'New Jersey')

# myTuple without New Jersey
printObj(myTuple)
line()

# Proves that this is still a tuple
print(type(myTuple),end='')
line()
