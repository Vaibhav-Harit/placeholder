import pygame as pg
import math
import random

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

    def decide_pos(self):
        pass
        #decided_pos = []

        #random_x = random.randint(100,500)
        #random_y = random.randint(100,500)
        #set_destination = ((self.x + random_x), (self.y + random_y))
        
chest1 = chest((100,500), pg.image.load('assets//interface//play.png'))

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    chest1.spawn(screen)

pg.display.flip()