partyPeople = []

while True:
    print('Please enter your name for the party. ' + 'If there are no other guests please hit enter: ')
    name = input()
    if name == "":
        break
    partyPeople = partyPeople + [name]
print('the guests names are: ')
for name in partyPeople:
    print(' ' + name)
