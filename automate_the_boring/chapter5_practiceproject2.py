# List to Dictionary Function for Fantasy Game Inventory
# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:


# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

def displayinventory(inventory):
    total_items = 0
    for k, v in inventory.items():
        print(k + ':' + str(v))
        total_items += v
    print("Total number of items is " + str(total_items))





inv = {'gold coin': 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayinventory(inv)

