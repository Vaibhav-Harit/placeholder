import pygame as pg
import math

class chest:
    def __init__(self, pos, sprite):
        self.img = sprite
        self.initial_position = pos
        self.x = pos[0]
        self.y = pos[1]

    def spawn(self, screen: pg.display):
        screen.blit(self.sprite, (self.x, self.y))

    def decide_pos(self):
        decided_pos = []

        random_x = random.randint(-1 * (range), range)
        random_y = random.randint(-1 * (range), range)
        set_destination = ((self.x + random_x), (self.y + random_y))
        

