#Lists

# contained in square brackets
# item
    # any value contained inside the list
    # separated BY COMMAS ,

spam = ['cat', 'bat', 'rat' 'elephant']
#INDEX      0,    1,     2,      3

print(spam[0])
print('Helloo ' + spam[1])

#numerical value inside spam is called the INDEX
#refers to the order of each word

#lists can also contain other lists values

spam = [['cat', 'bat'], [10, 20, 30, 40]]
print(spam[0])
print(spam[1][3])


#Negative Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])

#negative indexes begin within -1
    #pulls values from the end of the list -1, -2,


#Getting Sublists with Slices
# spam[2] - List w/an INDEX
# spam[1:4] - List w/a SLICE
    #first integer is where slice starts
    #second integer is where slice ends
#slices can get multiple values from a single lists
    #separated by a colon

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:4])
print(spam[0:-1])
print()
#shortcut
# you can leave the integer on either side of the colon out

print(spam[:3])
print(spam[1:])
print(spam[:])
print()

#len function will show how many items are within a list
print(len(spam))

# Changing Values in a List
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)

spam[2] = spam [1]
print(spam)

spam[-1] = 12345
print(spam)


#List Concatenation and List Replication
spam = [ 1, 2, 3]
print(spam + ['a', 'b', 'c'])

spammy = spam + ['a', 'b', 'c']
print(spammy * 3)

# Removing Values from Lists w/DEL Statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[0]
print(spam)
