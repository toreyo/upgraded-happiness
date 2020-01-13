
# Escape Characters
spam = 'hi this is Alice\'s cat'
print(spam)

print('Hi how are you doing today?\n I\'m feeling fantastic how about yourself? \n Great!')
print('\t this will be tabbed ')

# Raw strings
# place an r before quotation marks of a string to make it a raw string
# good for strings that contain many backslashes such as Windows file paths

print(r'this is Torey\'s raw string')

# F strings
name = 'Torey'
age = '27'

print(f"hi my name is {name} and I'm {age} years old. ")


spam = "hello world"
spam = spam.upper()
print(spam)

print(spam.isupper())

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

spam = ['cat', 'hat', 'bat']
spam.join(['cat', 'hat', 'bat'])
print(spam)


