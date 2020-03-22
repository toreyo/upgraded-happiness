# Regular Expressions
# Specific ways of searching for texts, ctrl + F, on steroids?
# requires raw strings
# re.compile(r'\d\d\d-\d\d\d\d)

import re
phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# match object
mo =  phoneNumbRegex.search('My number is 808-598-4256')
print('Phone number found: ' + mo.group())


Addresses ='''
7615 Rose Ave.
Pelham, AL 35124
8716 W. Hill Lane
Sulphur, LA 70663
9721 Ridgewood Circle
Rome, NY 13440
487 Mayfield Street
Xenia, OH 45385
74 Depot Street
Longview, TX 75604
9379 South Washington St.
Chesapeake, VA 23320
'''

adRegex = re.compile(r'\w\s, A-Z{2}\s\d{5}')
mo = adRegex.search(Addresses)

for x in mo:
    print('These are your city names, states, and zipcodes: ' + x)


