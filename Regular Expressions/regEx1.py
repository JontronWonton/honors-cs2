# Jonathan Klein
# 4/5/19
# regEx1.py

import re

def line(step='----'):
    print('-'*20 + step + '-'*20)

line(' part1 ')
name = 'Jonathan Klein'
matchName = re.match('Jonathan Klein', name)
print(matchName)
searchName = re.search('Jonathan', name)
print(searchName)

line(' part2 ')
txt = '15'
pattern = re.compile('15')
print(pattern.search(txt))

line(' part3 ')
txt = 'Friday'
pattern = re.compile('day')
if pattern.search(txt):
    print(True)
else:
    print(False)

line(' part4 ')
pattern = re.compile('[a-zA-Z0-9]')
print(pattern.search('foo'))
print(pattern.search('bar'))
print(pattern.search('baz'))
print(pattern.search('30'))
print(pattern.search('60'))
print(pattern.search('90'))

line(' part5 ')
def regExChecker(string, pat):
    pattern = re.compile(pat)
    if pattern.search(string):
        return True
    else:
        return False

print(regExChecker('RBRHS', '[A-Z]'))
print(regExChecker('HONORSCS2', '[A-Z]'))
print(regExChecker('JONATHAN KLEIN', '[A-Z]'))
print(regExChecker('Mr Watson', '\w'))
print(regExChecker('4/5/19', '[0-9]'))

line(' part6 ')
pattern = re.compile('\w{8}$')
print(pattern.search('jklein21'))
