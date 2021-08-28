import pygame as pg 
from functions.Helper_Functions import *


class Player(object):
    #initialization, will automatically run when you do a new instance
    def __init__(self, sprite : pg.image, screen_wh : tuple, pwr : int, spd : int, defense : int):
        self.power = pwr
        self.speed = spd
        self.defense = defense
        self.sprite = sprite
        self.position = center_coords(screen_wh, (sprite.get_width(), sprite.get_height()))

    def render(self, screen : pg.display):
        screen.blit(self.sprite, self.position)

    def attack(self, ):
        pass

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


    