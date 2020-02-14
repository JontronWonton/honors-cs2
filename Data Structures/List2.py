# Jonathan Klein
# 10/29/18
# List2.py

def line():
    print("-"*50)

def printNumList():
    for i in numList:
        print(i)

def addFive(a):
    for i in a:
        i += 5
        print(i)

def multNum(a):
    result = 1
    for i in a:
        result = i*result
    return result

def minNum(a):
    storage = a[0]
    for i in a:
        if i < storage:
            storage = i
    print(storage)

def maxNum(a):
    storage = a[0]
    for i in a:
        if i > storage:
            storage = i
    print(storage)

def addCommas(num):
    strNum = str(num)
    length = len(strNum)
    if length%3 == 0:
        return strNum[0:3]+","+strNum[3:6]+","+strNum[6:9]+","+strNum[9:12]+","+strNum[12:15]+","+strNum[15:18]
    elif length%3 == 1:
        return strNum[0]+","+strNum[1:4]+","+strNum[4:7]+","+strNum[7:10]+","+strNum[10:13]+","+strNum[13:16]
    elif length%3 == 2:
        return strNum[0:1]+","+strNum[2:5]+","+strNum[5:8]+","+strNum[8:11]+","+strNum[11:14]+","+strNum[14:17]



numList = [10, 20, 30, 69]

numList.append(100)
numList.append(200)
numList.append(300)
numList.append(400)
numList.append(420)
printNumList()
line()

del numList[0]
del numList[1]
printNumList()
line()

addFive(numList)
line()

print(multNum(numList))
line()

minNum(numList)
line()

maxNum(numList)
line()

print(addCommas(multNum(numList)))
line()
