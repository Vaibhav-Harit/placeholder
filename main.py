import pygame as pg
import math
import random


pg.init()
#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
screen = pg.display.set_mode([1350, 700])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED") 
   #icon later

#Player


#def



# loop (specially check this)
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# RGB FOR DISPLAY (CHANGE IT AS YOU WANT)
            screen.fill((0, 0, 0))

          
            pg.display.update()
