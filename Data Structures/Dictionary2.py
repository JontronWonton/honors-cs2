# Jonathan Klein
# 11/14/2018
# Dictionary2.py

def line():
    print('-'*50)


def printClassRoster():
    for i in class_roster:
        n = class_roster[i]['name']
        a = class_roster[i]['age']
        f = class_roster[i]['favSubject']
        print('{} is {} years old and loves {}'.format(n, a, f))


def printNewClassRoster():
    for i in class_roster:
        n = class_roster[i]['name']
        a = class_roster[i]['age']
        f = class_roster[i]['favSubject']
        t = class_roster[i]['totalClasses']
        print('{} is {} years old and loves {}. {} has {} total classes'.format(n, a, f, n, t))


class_roster_dictionary = {1 : { 'name': 'Matthew', 'age': 15, 'favSubject': 'Math'}, 2 : { 'name' : 'Jessica', 'age': 15, 'favSubject': 'English'}}

class_roster_dictionary2 = {
    1 : { 'name': 'Matthew', 'age': 15, 'favSubject': 'Math'},
    2 : { 'name' : 'Jessica', 'age': 15, 'favSubject': 'English'}
}

class_roster = {
    1 : {
    'name': 'Matthew',
    'age': 15,
    'favSubject': 'Math'
    },
    2 : {
    'name' : 'Jessica',
    'age': 15,
    'favSubject': 'English'
    }
}

fake_class_roster = {
    1 : {
    'name': 'Matthew',
    'age': 15,
    'favSubject': 'Math',
    'subjectList' : ['Math', 'Science', 'History', 'English'],
    'totalClasses' : 0
    },
    2 : {
    'name' : 'Jessica',
    'age': 15,
    'favSubject': 'English',
    'subjectList' : ['Math', 'Science', 'History', 'English'],
    'totalClasses' : 0
    }
}

print((class_roster[1]))
line()

print(class_roster[1]['name'])
line()

for i in class_roster:
    name = class_roster[i]['name']
    age = class_roster[i]['age']
    favSubject = class_roster[i]['favSubject']
    print('{} is {} years old and loves {}'.format(name, age, favSubject))
line()

class_roster[1]['favSubject'] = 'Computer Science'
printClassRoster()
line()

class_roster[2]['age'] += 1
printClassRoster()
line()

for i in class_roster:
    class_roster[i]['totalClasses'] = 5
    class_roster[i]['totalClasses'] = 5

printNewClassRoster()
line()

for i in fake_class_roster:
    fake_class_roster[i]['subjectList'].append('PE')
    fake_class_roster[i]['totalClasses'] = len(fake_class_roster[i]['subjectList'])

for i in fake_class_roster:
    print('''
Name: {}
Age: {}
Favorite Subject: {}
Subject List: {}
Total Classes: {}
    '''.format(fake_class_roster[i]['name'],
               fake_class_roster[i]['age'],
               fake_class_roster[i]['favSubject'],
               fake_class_roster[i]['subjectList'],
               fake_class_roster[i]['totalClasses']
               )
          )

line()
