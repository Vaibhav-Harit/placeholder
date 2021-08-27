import pygame as pg
import random
import math
import assets
from functions.Helper_Functions import *

pg.init()



#setting up the pygame window
clock=pg.time.Clock() 
screen = pg.display.set_mode([1350, 700]) #screen size

#variables
c_sprite = pg.image.load('assets//Character_sprite_placeholder.png')
play_sprite = pg.image.load('assets//play_sprite.png')

#this is the loop we'll code inside
running = True
while running:
    clock.tick(60)#DO NOT REMOVE THIS 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False #quits the pygame window when we click on X 

    

    screen.fill((0, 0, 0))
    pg.display.flip()




print ('code works')