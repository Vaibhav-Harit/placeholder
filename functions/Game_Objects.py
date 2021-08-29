import pygame as pg 
from functions.Helper_Functions import *


class Player(object):
    #initialization, will automatically run when you do a new instance
    def __init__(self, sprite : pg.image, screen_wh : tuple, pwr : int, spd : int, defense : int):
        #basic stats
        self.power = pwr
        self.speed = spd
        self.defense = defense
        
        #sprite, height and width
        self.sprite = sprite
        self.char_width = sprite.get_width()
        self.char_height = sprite.get_height()

        #position handling
        positon = center_coords(screen_wh, (sprite.get_width(), sprite.get_height()))
        self.x = positon[0]
        self.y = positon[1]

    def render(self, screen : pg.display):
        screen.blit(self.sprite, (self.x, self.y))

    def attack(self, ):
        pass

    def update_position(self, x_diff, y_diff):
        if x_diff >= 0:
            self.x += x_diff
        elif x_diff < 0:
            self.x -= abs(x_diff)

        if y_diff >= 0:
            self.y += y_diff
        elif y_diff < 0:
            self.y -= abs(y_diff)

    def sprint(self, ):
        pass

    def move(self, ):
        pass

    def block(self, ):
        pass

    def pick_up(self, ):
        pass

    def activate_skill(self, ):
        pass


    class Weapon(object):
        def __init__(self, sprite : pg.image, screen_wh : tuple, pwr : int, spd : int,):
            self.Wpower = pwr
            self.Wspeed = spd
            self.Wsprite = sprite

    