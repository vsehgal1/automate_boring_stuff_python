# game_inv.py
# automatetheboringstuff.com Chapter 4
# Vikram Sehgal

def displayInventory (inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory (inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1

    return inventory

if __name__ == "__main__":
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)