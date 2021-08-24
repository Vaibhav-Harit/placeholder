import pygame as pg
import random

pg.init()

#setting up the pygame window
clock=pg.time.Clock() 
screen = pg.display.set_mode([500, 500]) #screen size
square = pg.Surface((20, 20)) #idk lol
square.fill((255, 255, 255)) #screen color, RGB
rect = square.get_rect() #creates a square

#to end the game 
screen.fill((0, 0, 0))
screen.blit(square, rect)
pg.display.flip()