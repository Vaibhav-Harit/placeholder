import pygame as pg
import pandas
import random

chest_cords_list = [
            (100,100),
            (300,300),
            (500,500),
            (700,700)]
chest_cords = random.choice(chest_cords_list)
chest_x = chest_cords_list[0]
chest_y = chest_cords_list[1]


#chest_item class
class Chest_Item:
    def __init__(self, name, drop_rate, ID):
        self.name = name
        self.drop_rate = drop_rate
        self.ID = ID


class chest:
    def __init__(self, pos, sprite):
        self.img = sprite
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

    def spawn(self, screen: pg.display):
        screen.blit(self.img, (self.x, self.y))

    #def loot(self):

    
#creating a dictionary for chest_item objects
def chest_items_init(chest_items_dict):
    chest_item_list = {}
    for chest_item in chest_items_dict:
        chest_item_list[chest_item['ID']] = Chest_Item(chest_item['Name'], chest_item['Drop Rate'], chest_item['ID'])
    return chest_item_list

#initializing chest_item_list
chest_items_df = pandas.read_excel('assets\lists\item_list.xlsx', sheet_name = 'ChestDrops')
chest_items_dict = chest_items_df.to_dict('records')
chest_list = chest_items_init(chest_items_dict)

#making the values for randomizing




