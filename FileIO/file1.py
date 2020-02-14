# Jonathan Klein
# 1/31/2019
# file.py

quote = '''We have a very close relationship but we are NOT friends.
'''

wf = open('quote.txt', 'w')
wf.write(quote)

wf.close()

#--------------------------------------------------------------

rf = open('quote.txt', 'r')
data = rf.read()

print(data)

rf.close()

#--------------------------------------------------------------

quote2 = '''I would much rather you take the L than cheat.
'''

af = open('quote.txt', 'a')
af.write(quote2)

af.close()

af = open('quote.txt', 'r')
data = af.read()

print(data)

af.close()

#--------------------------------------------------------------

quote3 = '''Jason that's gonna cost you next time
...
Actually you know what Jason that's gonna cost you right now.
'''

def write2file(filename, string):
    f = open(filename, 'w')
    f.write(string)
    f.close()

def readFile(filename):
    f = open(filename, 'r')
    for line in f:
        print(line, end='')

write2file('another_quote.txt', quote3)
readFile('another_quote.txt')

#--------------------------------------------------------------

quote4 = '''I don't understand why you guys have girlfriends at such a young age.
I didn't have a girlfriend until I was 16!
'''

def append2file(filename, string):
    f = open(filename, 'a')
    f.write(string)
    f.close()

append2file('quote4.txt', quote4)
readFile('quote4.txt')

#--------------------------------------------------------------

bonus = open('poem.txt', 'r')

for i, line in enumerate(bonus):
    if i == 2:
        print(line, end='')

bonus.close()
bonus = open('poem.txt', 'r')

for j, line in enumerate(bonus):
    if j%2 == 1:
        print(line, end='')

bonus.close()

#--------------------------------------------------------------
