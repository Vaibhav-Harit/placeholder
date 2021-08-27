import pygame as pg
import random
a = 0

pg.init()

#setting up the pygame window
clock=pg.time.Clock() 
screen = pg.display.set_mode([500, 500]) #screen size
square = pg.Surface((20, 20)) #creates a surface with a given width and height
square.fill((255, 255, 255)) #screen color, RGB
rect = square.get_rect() #creates a square


#this is the loop we'll code inside
running = True
while running:
    clock.tick(60)#DO NOT REMOVE THIS 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False #quits the pygame window when we click on X 
    rect.x = 240
    rect.y = 240
    screen.fill((0, 0, 0))
    screen.blit(square, rect)
    pg.display.flip()

print ('code works')