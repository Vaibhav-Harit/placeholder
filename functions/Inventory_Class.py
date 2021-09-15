import pandas

#----------ITEMS CLASS----------#
class Item:
    def __init__(self, name, type, rarity, ID, sprite = None, description = None, item_class1 = None, item_class2 = None, power = None, speed = None):
        self.name = name
        self.type = type
        self.rarity = rarity
        self.ID = ID
        self.sprite = sprite
        self.first_class = item_class1
        self.second_class = item_class2
        self.power = power
        self.speed = speed
        self.description = description

def initialize_items(items_dict):   #a function to initialize all items in a processed dictionary
    item_list = {}
    for item in items_dict:
        item_list[item['Item ID']] = Item(item['Item Name'], item['Item Type'], item['Item Class Set'], item['Item ID'], item['Sprite'], item['Description'], item['Class Type 1'], item['Class Type 2'], item['Power'], item['Speed'])
    return item_list

#initializing items through functions
items_df = pandas.read_excel('assets\lists\item_list.xlsx', sheet_name = 'ItemList')
item_dictionary = items_df.to_dict('records')
item_list = initialize_items(item_dictionary)

#----------INVENTORY SYSTEM----------#
class Inventory:
    #a dictionary with all the items in the game {item_ID: item_name}
    item_list = {}

    def __init__(self):
        #a dictionary containing the item_ID and amount in inventory
        self.items = {}

    #adds an item to the player inventory
    def add_item(self, item_ID, amount):
        if item_ID in self.items:
            self.items[item_ID] += amount
        else:
            self.items[item_ID] = amount

    #removes an item from player inventory
    def remove_item(self, item_ID, amount):
        if item_ID in self.items:
            self.items[item_ID] -= amount
            if self.items[item_ID] == 0:
                self.items.pop(item_ID) #removes the itemID from inventory if the amount is zero
        #-----You can add an else statement if you have anything you want it to do if the item is not present-----#

    #sorts the inventory by item type // first item ID digit
    def inv_type_sort(self):
        sorted_inventory = sorted(self.items.items(), key = lambda x: int(str(x[0])[0:]))
        self.items = {}
        for item in sorted_inventory:
            itemID = item[0]
            item_amount = item[1]
            self.items[itemID] = item_amount

    #sorts the inventory by item rarity // second item ID digit
    def inv_rarity_sort(self):
        sorted_inventory = sorted(self.items.items(), key = lambda x: int(str(x[0])[1]))
        self.items = {}
        for item in sorted_inventory:
            itemID = item[0]
            item_amount = item[1]
            self.items[itemID] = item_amount

    #sorts the inventory by class type of the item (exclusive for weapons) // third item ID digit
    def inv_class_sort(self):
        sorted_inventory = sorted(self.items.items(), key = lambda x: int(str(x[0])[2]), reverse = True)
        self.items = {}
        for item in sorted_inventory:
            itemID = item[0]
            item_amount = item[1]
            self.items[itemID] = item_amount
    
    #how to display greedo help xD
    def display_inventory(self):
        pass

