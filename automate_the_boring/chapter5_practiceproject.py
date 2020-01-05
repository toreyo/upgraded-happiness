# Fantasy Game Inventory
# You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

# Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

inventory = {'weapons': {'dagger': 3, 'sword': 1, 'bow': 1, 'arrow': 20}, 'potions' : {'health': 4, 'mana': 3, 'rage': 2} }

def displayInventory(bag, items):
    numBrought = 0
    for k, v in bag.items():
        numBrought += v.get(items, 0)
    return(numBrought)

print('These are your weapons and potions that are available: ')
print(' - dagger: ' + str(displayInventory(inventory, 'dagger')))
print(' - sword: ' + str(displayInventory(inventory, 'sword')))
print(' - bow: ' + str(displayInventory(inventory, 'bow')))
print(' - arrow: ' + str(displayInventory(inventory, 'arrow')))
print(' - health potions: ' + str(displayInventory(inventory, 'health')))
print(' - mana potions: ' + str(displayInventory(inventory, 'mana')))
print(' - rage potions: ' + str(displayInventory(inventory, 'rage')))


#
