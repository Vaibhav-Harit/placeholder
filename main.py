import pygame
import math
import random

# initialize pygame (Check all the work greed - AJ)
pygame.init()

# screen
screen=pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("NOT DECIDED")

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # RGB FOR DISPLAY (CHANGE IT AS YOU WANT)
            screen.fill((129, 129, 129))
            pygame.display.update()