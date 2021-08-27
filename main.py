import pygame as pg
import math
import random


pg.init()

<<<<<<< HEAD

screen=pg.display.set_mode((1350, 700)) #screen size
clock=pg.time.Clock()


pg.display.set_caption("NOT DECIDED")
#icon = pg.image.load('-')
#pg.display.set_icon(icon)

#Player

=======
# Title/Icon (Nothing is Decided)
pygame.display.set_caption("NOT DECIDED") 
   #icon later

#Player


#def

>>>>>>> e2a6b12fcaf48f234f4733cbd4aada1db551308f


# loop (specially check this)
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

<<<<<<< HEAD

    screen.fill((0, 0, 0))
    pg.display.update()
=======
# RGB FOR DISPLAY (CHANGE IT AS YOU WANT)
            screen.fill((0, 0, 0))

          
            pygame.display.update()
>>>>>>> e2a6b12fcaf48f234f4733cbd4aada1db551308f
