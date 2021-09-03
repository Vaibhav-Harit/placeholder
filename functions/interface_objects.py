import pygame as pg
import random
import math

class button(object):
    def __init__(self, name: str, sprite: pg.image, position: tuple)
        self.buttonname = name
        self.buttonimg = sprite
        self.cords = position

        self.x = position[0]
        self.y = position[1]

        def draw(self, screen: pg.display):
            screen.blit(self.sprite, (self.x, self.y))