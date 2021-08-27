import pygame
import math
import random

# initialize pygame (Check all the work greed - AJ)
pygame.init()

# screen (Not Decided Too)
screen=pygame.display.set_mode((800, 600))

# Title/Icon (Nothing is Decided)
pygame.display.set_caption("NOT DECIDED") 
   #icon later

#Player


#def



# loop (specially check this)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# RGB FOR DISPLAY (CHANGE IT AS YOU WANT)
            screen.fill((0, 0, 0))

          
            pygame.display.update()