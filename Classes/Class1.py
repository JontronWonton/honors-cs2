# Jonathan Klein
# 12/12/18
# Class1.py

import datetime


class Student:
    def __init__(self, name, age, favSubject):
        self.name = name
        self.age = age
        self.favSubject = favSubject.lower()

    def greeting(self):
        print(f'Hello, {self.name}. You are {self.age} years old and you {self.favSubject}.')

    def birthday(self):
        self.age += 1
        print(f'Happy birthday {self.name}! You\'re now {self.age} years old!')

    def birthYear(self):
        year = datetime.datetime.now().year - self.age
        print(f'{self.name} was born during {year}')


kenneth = Student('Kenneth', 15, 'CS 2')
cameron = Student('Cameron', 15, 'Biomedical')
nick = Student('Nick', 15, 'Networking')


# kenneth.greeting()
# cameron.greeting()
# nick.greeting()
#
# kenneth.birthYear()
# cameron.birthYear()
# nick.birthYear()
#
# kenneth.birthday()
# cameron.birthday()
# nick.birthday()
