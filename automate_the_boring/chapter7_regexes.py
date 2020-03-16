# Regular Expressions
# Specific ways of searching for texts, ctrl + F, on steroids?
# requires raw strings
# re.compile(r'\d\d\d-\d\d\d\d)

import re
phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# match object
mo =  phoneNumbRegex.search('My number is 808-598-4256')
print('Phone number found: ' + mo.group())
