#For loops with Lists
#a common technique
    # range(len(someList))
    # with a forLoop to iterate over indexes of a list.

supplies = ['pen', 'paper', 'flamethrower', 'binder']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is ' + supplies[i])


#In and Not Operators
spam = ['hello', 'hi', 'howdy', 'heya']
print('cat' in spam)


#Multiple Assignemnt Trick
# lets you asign multiple variables with values in one line of code

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

#Augmented Assignment Operators
#
