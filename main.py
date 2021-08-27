import pygame
import math
import random

# initialize pygame (Check all the work greed - AJ)
pygame.init()

# screen (Not Decided Too)
screen=pygame.display.set_mode((800, 600))

# Title/Icon (Nothing is Decided)
pygame.display.set_caption("NOT DECIDED")
icon = pygame.image.load('-')
pygame.display.set_icon(icon)

#Player
square = pg.Surface((20, 20)) #creates a surface with a given width and height
rect = square.get_rect() #creates a square


# loop (specially check this)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect.x = 240
    rect.y = 240 

            # RGB FOR DISPLAY (CHANGE IT AS YOU WANT)
            screen.fill((0, 0, 0))
            pygame.display.update()