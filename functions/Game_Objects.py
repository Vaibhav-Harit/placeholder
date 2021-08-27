import pygame as pg 
import math
import assets

sprite_1 = pg.image.load("dungeon_tiles.png")


class Player(object):
    #initialization, will automatically run when you do a new instance
    def __init__(self, pwr, spd, defense, sprite, position, direction):
        self.power = pwr
        self.speed = spd
        self.defense = defense
        self.sprite = sprite
        self.position = position
        self.direction = direction

    def attack():
        pass

    def sprint():
        pass

    def move():
        pass

    def block():
        pass

    def pick_up():
        pass

    def activate_skill():
        pass

    def draw():
        pg.blit(self.sprite, self.position )
    
    charac_1 = Player(10, 10, 10, sprite_1, (250,250), 0)