# Jonathan Klein
# 10/23/18
# List1.py

nameList = ["Maurice", "Humphrey", "Jeremiah", "Adrian"]


def line():
    print("-"*15)


def printList():
    for i in nameList:
        print(i)


def miniStory():
    return f"Hi {nameList[0]}\nHi {nameList[1]}\nHi {nameList[2]}\nHi {nameList[3]}"


for i in nameList:
    print(i)
line()


print(nameList[0])
print(nameList[1])
print(nameList[2])
print(nameList[3])
line()

print("Jeremiah is at index", nameList.index("Jeremiah"))
line()

print("The length of my list is", len(nameList))
line()

printList()
line()

nameList.append("Watson")
nameList.append("Richard")
nameList.append("Theodore")
printList()
line()

nameList.remove("Maurice")
nameList.remove("Humphrey")
printList()
line()

del nameList[len(nameList)-1]
printList()
line()

print(miniStory())
