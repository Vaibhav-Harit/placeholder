import pygame as pg
import random
import math

class button(object):
    def __init__(self, name: str, trigger: str, sprite: pg.image, position: tuple)
        self.buttonname = name
        self.trigger = trigger
        self.buttonimg = sprite
        self.cords = position

        self.x = position[0]
        self.y = position[1]

        def draw(self, screen: pg.display):
            screen.blit(self.sprite, (self.x, self.y))

        def clicked(self)
        if pg.mouse.get_pressed()[0] and name.rect.collidepoint(pg.mouse.get_pos()) and not handled:
            pass