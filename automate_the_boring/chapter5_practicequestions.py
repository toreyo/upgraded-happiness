#
# Q:
#
# 1. What does the code for an empty dictionary look like?
#
emptyDictionary = {}
#
#
# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
#
foo42 = {'foo': '42'}
#
# 3. What is the main difference between a dictionary and a list?
#
# dictionary not in a set order, usually have 2 or more corresponding objects, a key and a variable
# lists follow an index and are in a set order
#
# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
#
# Q: Error
#
# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
#
# Q: There is no difference
#
# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
#
# Q: 'cat' in spam will check for keys, while 'cat' in spam.values() will look for cat only in the values
#
# 7. What is a shortcut for the following code?
#
#
# if 'color' not in spam:
#     spam['color'] = 'black'

# Q: spam.setdefault('color', 'black')
#
# 8. What module and function can be used to “pretty print” dictionary values?
# import pprint
# pprint.pprint('insert dictionary here')



