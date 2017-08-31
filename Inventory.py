def length_of_longest_key(inventory):
    print(inventory)
    lngst = "a"
    inv = inventory.keys()
    for it in inv:
        if len(it) > len(lngst):
            lngst = it
    return len(lngst)


def length_of_longest(inventory, counter):
    print(inventory)
    lngst = "a"
    for it in inventory:
        if len(it) > len(lngst):
            lngst = it
    return len(lngst)


def inventory():
    inv = {'shirt': [0, 1, "cloth", 70], 'sword': [0, 1, "weapon", 100], 'gold coin': [1, 42, "gold", 100]}
    l = length_of_longest_key(inv)
    w = length_of_longest(inv, 3)
    it = length_of_longest(inv, 2)
    bar = (100 * "-")
    print("Inventory:\n"+"Item Name".rjust(l, " ") + "Count".rjust(10, " ") + "Weight".rjust(w + 4, " ") 
          + "Item Type".rjust(it + 4, " "), "\n"+bar)
    for i in inv:
        if inv[i][0] == 0:
            continue
        else:
            item = str(i)
            count = str(inv[i][1])
            weight = str(inv[i][3])
            item_type = str(inv[i][2])
            print("{} {} {} {}".format(item.rjust(l, " "), count.rjust(9, " "), weight.rjust(w + 3, " "), item_type.rjust(it + 3, " ")))

inventory()