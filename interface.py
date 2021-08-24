#DO NOT RUN THE CODE
import pygame as pg
import random
a = 0

pg.init()

#setting up the pygame window
clock=pg.time.Clock() 
screen = pg.display.set_mode([500, 500]) #screen size
square = pg.Surface((20, 20)) #idk lol
square.fill((255, 255, 255)) #screen color, RGB
rect = square.get_rect() #creates a square

#this is the loop we'll code inside
while True:
    event = pg.event.poll()
    if event.type == pg.QUIT:
        exit()