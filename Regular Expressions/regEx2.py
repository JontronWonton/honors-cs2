# Jonathan Klein
# 4/9/19
# regEx2.py

import re

def line():
    print('='*50)

def regExChecker(string, pat):
    pattern = re.compile(pat)
    return pattern.search(string)

# environmental strings
rbrhsUN = 'jklein21'
password = 'Passw0rd!'
email = 'legit-email101@website123.com'
twitterUN = 'adrian_wilk'
url = 'www.example.com'
facebookURL = 'www.facebook.com/zuck'
ipv4 = '192.168.0.1'
ipv6 = '1200:0000:AB00:1234:0000:2552:7777:1313'
date1 = '04/09/2019'
date2 = '04/09/19'
pn1 = '(555)555-5555'
pn2 = '555-555-5555'
pn3 = '5555555555'

line()
print(regExChecker(rbrhsUN, '^([a-z]*)+(\d{2})$'))

line()
print(regExChecker(password, '((?=(.*[0-9]))(?=.*[\!@#$%^&*()\\\[\]\{\}\-+=;:<>?,.])(?=(.*[A-Z])))^.{8,15}$'))
# 8 Letters
# 1 number
# 1 special character
# 1 capital letter

line()
print(regExChecker(email, '(^[\w\d-]+@[a-z\d-]+\.[a-z]{2,3}$)'))

line()
print(regExChecker(twitterUN, '(^[a-zA-Z0-9_]{1,15}$)'))

line()
print(regExChecker(url,'(www\.)?[a-zA-Z0-9@:%._\+~#=]{2,20}\.[com]'))

line()
print(regExChecker(facebookURL, '(www\.)?[a-zA-Z0-9@:%._\+~#=]{2,20}\.[com]+/+[a-zA-Z0-9@:%._\+~#=]{2,20}'))

line()
print(regExChecker(ipv4, '(\d){1,3}.(\d){1,3}.(\d){1,3}.(\d){1,3}'))
