catNames = [] #why do we need this, if we have list concatenation down below

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1)  + '( Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  #list concatenation
print('the cat names are: ')
for name in catNames:
    print(' ' + name)
