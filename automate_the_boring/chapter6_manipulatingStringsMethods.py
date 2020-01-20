# The is Xmethods()
# returns a boolean value
# x.isalpha returns True only if string contains alphabets only and isn't blank
# x.isalnum returns True only if string contains alphabets and decimals only and isn't blank
# x.istitle returns True only if string contains words where only the first letter is capital and the rest are lower case and isn't blank
# x.isdecimal returns True only if string contains numbers and isn't blank
# x.isspace returns True only if string contains spaces, tabs, and new lines and isn't blank

hello = 'hello123'
print(hello.isalpha())


# Starts and ends with methods()
# startswith() and endswith()
# similar function to is == , but can validate strings without having to enter in full string name

sent = 'hello my name is stringy string feeling a strictly stringent'
print(sent.startswith('hello my name is'))
print(sent.endswith('stringent'))

# Join and Split Methods
# join method is useful when you have a list of strings that need to be joined together

# spam = ['cat', 'hat', 'bat']
print('spam'.join(['cat', 'hat', 'bat']))
print(', '.join(['cat', 'hat', 'bat']))
print(''.join(['cat', 'hat', 'bat']))

# Split method
print('My name is Torey'.split())
spam = '''
Hello the name is Torey
How are you doing today
Today is a game-changing day of the year
Lot's of expelling of lifestyle disease waste for the year
Year of Intention baby
'''

spam = spam.split('\n')
print(spam)

# Partition Method
# Splits into three substrings
# "before", "separator", "after"

spam = 'Hi my name is Rodger Rabbit'
spam = spam.partition('Rodger')
print(spam)

world = 'Hello World!'
world = world.partition('ello')
print(world)

cstring = 'this is a center string'
print(cstring.center(40, '*'))
print(cstring.center(40))

lstring = 'this a is a left string'
print(lstring.ljust(40, '-'))

rstring = 'this is a right string'
print(rstring.rjust(40, '-'))
print(rstring.rjust(40))

# Strip methods
# Used to remove spaces, tabs or new lines on LEFT, RIGHT, or BOTH

spam = '    hello, world      '
print(spam.strip())

print(spam.lstrip())
print(spam.rstrip())


spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
# strips from 'ampS' from both left and right sides of the string,  the order does not matter

print(ord('A'))
