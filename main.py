from functions.Helper_Functions import center_coords
import pygame as pg
import math
import random
import assets

pg.init()
#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
screen = pg.display.set_mode([1350, 700])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED") 
   #icon later

#Player
charac_sprite = pg.image.load('assets//dungeon_tiles.png')

#def
def player():
    screen.blit(charac_sprite, center_coords((1350, 700), (50, 50)))


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