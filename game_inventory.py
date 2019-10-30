inventory = {'line': 1, 'torch': 6, 'gold': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k, v)
        item_total += v
    print('Total number of items: ' + str(item_total))

dragonLoot = ['gold', 'dagger', 'gold', 'gold', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1

displayInventory(inventory)
addToInventory(inventory, dragonLoot)
displayInventory(inventory)