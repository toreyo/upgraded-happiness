birthday = {'Jordyn': 'November 28', 'Johanna': 'December 12', 'CJ': 'January 4'}

while True:
    print('Enter a name (or enter nothing to quit): ')
    name = input()
    if name == '':
        break
    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print("I don't have information for that person.")
        print('What is their birthday? ')
        bday = input()
        birthday[name] = bday
        print('Birthday database updated. ')
