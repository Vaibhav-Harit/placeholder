import pygame as pg
import math
import random
from Helper_Functions import *

clock=pg.time.Clock()
sc_width = 1300
sc_height = 700
screen = pg.display.set_mode([sc_width, sc_height])

class chest:
    def __init__(self, pos, sprite):
        self.img = sprite
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

    def spawn(self, screen: pg.display):
        screen.blit(self.img, (self.x, self.y))

# we're testing the chest here as of now, will remove later
random_x = random.randint(100,1000)
random_y = random.randint(100,1000)
cords = ((random_x), (random_y))
        
chest1 = chest((cords), pg.image.load('assets//interface//play.png'))

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    chest1.spawn(screen)

    pg.display.flip()