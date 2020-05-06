# KEYS VALUES AND ITEMS METHODS
favColors = {'Johanna': 'pink', 'Sam': 'brown', 'Torey': 'blue'}


for k in favColors.keys():
    print(k)
print()

# Keys will print FIRST part of each dictionary item


for v in favColors.values():
    print(v)
print()
# Values will print SECOND part of each dictionary item


for i in favColors.items():
    print(i)
print()

# Items will print EVERYTHING of dictionary


print(favColors.keys())
print()

# prints a tuple version

print(list(favColors.keys()))
print()

# prints a list version


# GET METHOD
# to determine if key exists in a dictionary
# dictionaryName.get('item', 0) - 0 is implemented to return, incase there is no item in the dictionary

partyItems = {'beer': '3', 'wine': '2', 'hards': '1'}
print('I am bringing ' + str(partyItems.get('beer', 0)) + ' beer bottles')
print('I am bringing ' + str(partyItems.get('cheese', 0)) + ' cheese trays')

print()
print(partyItems.get('wine', 0))
print()

# Set Default also to determine if key exists in dictionary, if not you can set value in dictionary
popClothes = {'tshirt': '3', 'pants': '7'}
if 'shoes' not in popClothes:
    popClothes['shoes'] = '5'

for i in popClothes.items():
    print(i)
print()


popClothes.setdefault('hats', '10')
for i in popClothes.items():
    print(i)
print()

for k in popClothes.keys():
    print(k)
print()

# Character count
message = "I went to go eat with my family yesterday at Uncle Blake's house. I'm looking forward to meeting Emily. "
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
print()


# Pretty Printing - Pprint

import pprint
message = "I went to go eat with my family yesterday at Uncle Blake's house. I'm looking forward to meeting Emily. "
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)




