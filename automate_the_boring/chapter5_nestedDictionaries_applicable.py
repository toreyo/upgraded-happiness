allGuests = {'Torey': {'money' : 50, 'gift': 1}, 'Taylor': {'money': 25, 'gift':2}, 'Ty': {'money' : 100, 'gift': 3} }

def totalBrought(guests, items):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(items, 0)
    return numBrought

print('Amount of money and number of gifts that were given: ')
print(' - Money ' + str(totalBrought(allGuests, 'money')))
print(' - Gifts ' + str(totalBrought(allGuests, 'gift')))



