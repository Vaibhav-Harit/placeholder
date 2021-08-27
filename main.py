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
charac_sprite = pg.image.load('assets//Character_sprite_placeholder.png')

#def
def player():
    screen.blit(charac_sprite, center_coords((1350, 700), (50, 50)))


#Game loop
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    

    screen.fill((0, 0, 0)) #screen color RGB

    player()
    pg.display.update()