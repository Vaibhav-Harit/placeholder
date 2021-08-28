from functions.Helper_Functions import center_coords
import pygame as pg
import math
import random
import assets

pg.init()
#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
sc_width = 600
sc_height = 600
screen = pg.display.set_mode([sc_width, sc_height])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED")

#Player
charac_sprite = pg.image.load('assets//Character_sprite_placeholder.png')
ch_width = charac_sprite.get_width()
ch_height = charac_sprite.get_height()

#def
def player():
    screen.blit(charac_sprite, center_coords((sc_width, sc_height), (ch_width, ch_height)))


#Game loop
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    

#Key Presses
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x -= vel        
    if keys[pg.K_RIGHT]:
        x += vel
    if keys[pg.K_UP]:
        y -= vel
    if keys[pg.K_DOWN]:    
        y += vel


    screen.fill((0, 0, 0)) #screen color RGB

    player()
    pg.display.update()