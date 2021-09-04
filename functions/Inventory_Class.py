class Inventory():
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
                self.items.pop(item_ID) #removes the key from the inventory if the item does not exist
        #-----You can add an else statement if you have anything you want it to do if the item is not present-----#

    def display_inventory(self):
        pass


