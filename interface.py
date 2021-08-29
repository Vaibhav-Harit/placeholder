import pygame as pg
import random
import math
import assets
from functions.Helper_Functions import *


pg.init()



#setting up the pygame window
clock=pg.time.Clock() 
screen = pg.display.set_mode([1350, 700]) #screen size 

#Menu
main_menu = True

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):

        screen.blit(self.image, self.rect)

#Buttons-Sprites
start_img = pg.image.load('assets//other//play_sprite.png')
options_img = pg.image.load('assets//other//options_sprite.png')
credits_img = pg.image.load('assets//other//credits_sprite.png')

#Creating/to screen/coords
start_button = Button(530, 330, start_img)
options_button = Button(530, 450, options_img)
credits_button = Button(530, 570, credits_img)

#this is the loop we'll code inside
running = True
while running:
    clock.tick(60)#DO NOT REMOVE THIS 
   
    #Menu    
    if main_menu == True:
        start_button.draw()
        options_button.draw()
        credits_button.draw()
    else:
        print("xD")
         
#EventPanel         
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False #quits the pygame window when we click on X 



   

    screen.fill((255, 255, 255))
    start_button.draw()
    options_button.draw()
    credits_button.draw()
    pg.display.flip()