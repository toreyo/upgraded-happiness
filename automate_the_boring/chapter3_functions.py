# functions
# print(), input(),
# len() - returns number of items in an object, or characters in a string

# def statements
# defines a function
# work similarly to variables
# can assign multiple definitions to a function
from abc import ABC


def hello(name):
    print("Hello " + name)


hello('Alice ')
hello('Bob ')

# return statement
# can specify what is returned in a define statement

# keyword arguements and print
# identified by the keyword put before them in function call
# used for optional functionality
# eg. print has sep and end
#  to identify what it should print between and at the end of its arguements

print('Hello')
print('world')

print('Hello', end='')
print('world')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')

# local&global scope
# local refers to variables within a function
# global refers to variables that are within the program in its entirety
# main tip is to have separate named variables for local and global variables

#Exception Handling
#

