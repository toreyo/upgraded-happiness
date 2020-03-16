import re

textToSearch = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLKMNOPQRSTUVWXYZ123456789
'''
sent = 'This is a random sentence about how I am learning to code today about regular expressions'
pattern = re.compile(r'abc')

mo = pattern.finditer(textToSearch)
for match in mo:
    print(match)

print(textToSearch[0:3])


