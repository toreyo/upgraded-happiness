import os
from pathlib import Path
import shelve

# showing the current working directory
# print(os.getcwd())
# print(Path.cwd())
#
# x = (Path.cwd())

# making new folder directories with os.makedirs()
# os.makedirs('This/is/a/test/yo')


# reading and writing files 
# newText = open('practice.txt', 'w')
# newText.write("Hello this is a new test and I'm practicing")
# newText.close()

# Storing variables in shelve files 
# import shelve
# create a variable that will store in shelve's open method
# create lists, that will be stored as dictionaries
stored = shelve.open('mydata')
rabbits = ['harry', 'hare', 'rodgers']
dogs = ['nike', 'kuma', 'bruno', 'mochi', 'berry']
cats = ['sammie']

stored['rabbits'] = rabbits
stored['dogs'] = dogs
stored['cats'] = cats

stored.close()
