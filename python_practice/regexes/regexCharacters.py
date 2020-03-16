# .  - Any character except a new line
# \d - digits (0-9)
# \D - non-digits (anything, but 0-9)
# \w - word characters (a-z, A-Z, 0-9, _)
# \W - non-word characters
# \s - whitespaces (space, tab, newline)
# \S - non-whitespaces

# \b - word Boundry(boundaries before work, beginning of the line or spaces count as word boundaries)
# \B - non-word boundry
# ^ beginning of a string
#  $ end of a string



import re

textToSearch = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLKMNOPQRSTUVWXYZ123456789

Ha HaHa

808.547.4562
808-756-7815

'''

sentence = 'This is the start and this is the end of the sentence'

patternFinder = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
mo = patternFinder.finditer(textToSearch)
for matches in mo:
    print(matches)

