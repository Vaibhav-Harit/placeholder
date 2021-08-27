import pygame as pg
import math
import random


pg.init()


screen=pg.display.set_mode((1350, 700)) #screen size
clock=pg.time.Clock()


pg.display.set_caption("NOT DECIDED")
#icon = pg.image.load('-')
#pg.display.set_icon(icon)

#Player



# loop (specially check this)
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill((0, 0, 0))
    pg.display.update()