#For loops with Lists
#a common technique
    # range(len(someList))
    # with a forLoop to iterate over indexes of a list.

#USEFUL
supplies = ['pen', 'paper', 'flamethrower', 'binder']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is ' + supplies[i])

#USEFUL
#In and Not Operators
spam = ['hello', 'hi', 'howdy', 'heya']
print('cat' in spam)


#Multiple Assignemnt Trick
# lets you assign multiple variables with values in one line of code

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

#Augmented Assignment Operators
# spam += 1    spam = spam +1
# spam -= 1    spam = spam - 1
# spam *=1     spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

spam = 'Hello'
spam += 'World'

print(spam)

bacon = ['cherrybrah']
bacon *= 3
print(bacon)

# Methods
# attached to a variabe? via a  period
#     eg. if spam is holding a list value
#           spam.index()

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('heyas'))

poppingStyles = ['boogaloo', 'tutting', 'robotting', 'hitting', 'animation', 'dimestop']
print(poppingStyles.index('tutting'))

# Adding values to a list w/ Append and Insert Methods
# append and insert are LIST METHODS
spam = ['cat', 'dog', 'bat']
spam.append('moose') #Append will add a value at the END of a LIST
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken') #Insert can add a value at a specific location. Enter index you want it at, and the value you want to insert
print(spam)

# Removing values from a list w/ Remove Method
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
del(spam[0])
print(spam)

# Sorting values in a list w/Sort Method
spam = [3, 54,5, 6, 3, 2, 5, 7, 7, 12 , 2345, 2323, 67, 86, 90, 1]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = ['rodger', 'wily', 'alpha', 'beta', 'carotene', 'billy', 'zinc', 'xylophone']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

# Important to note
# Alphabetical values get sorted by capitals ABC then lower case abc
spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)

# if you want to change this then:

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)


# Simlarities in Strings and Lists
# Many things you can do with lists can be done with strings too
name = 'Torey'
print(name[0])
print(name[-2])
print(name[0:3])
print('z' in name)
print('T' in name)
for i in name:
    print('***' + i + '***')

