# Tuples are similar to lits, BUT are IMMUTABLE (Can't be changed)

print(type(('hello',)))
print(type(('hello')))

print(tuple(['cat', 'dog', 'hat']))
print(list(('cat', 'dog', 'hat')))
print(list('hello'))
print()


# Copy and Deep Copy Modules
# Important and are used when you need to change the dictionary or lists, but still need a copy of the original

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(cheese)
print(spam)

#deep copy will allow you to copy lists...WITHIN lists
