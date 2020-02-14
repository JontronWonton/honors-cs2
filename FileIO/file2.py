# Jonathan Klein
# 2/4/19
# file2.py

with open('story.txt') as f:
    story = f.readlines()
    for i, line in enumerate(story):
        if i == 0:
            print(line)

print('='*50)

with open('story.txt') as f:
    story = f.readlines()
    for i, line in enumerate(story):
        if i == len(story)-1:
            print(line)

print('='*50)

with open('story.txt') as f:
    story = f.readlines()
    for i, line in enumerate(story):
        if i % 2 == 1:
            print(line)

print('='*50)

with open('story.txt') as f:
    story = f.readlines()
    for i, line in enumerate(story):
        if i % 2 == 0:
            print(line)

print('='*50 + '\nPART 2:\n' + '='*50)

with open('names.txt') as f:
    name_list = f.readlines()
    for line in name_list:
        print(line)

print('='*50)

with open('names.txt') as f:
    name_list = f.readlines()
    for line in name_list:
        if line.lower().startswith('i'):
            print(line)

print('='*50)

with open('names.txt') as f:
    name_sorted = sorted(f.readlines())
    with open('names_sorted.txt', 'w') as f:
        for i in name_sorted:
            f.write(i)

def add2names(name):
    with open('names.txt', 'a+') as f:
            f.write(name + '\n')

add2names('Rebecca')
