import pygame as pg
import random
import math
import assets
from functions.Helper_Functions import *


pg.init()



#setting up the pygame window
clock=pg.time.Clock() 
sc_width = 1350
sc_height = 690
screen = pg.display.set_mode([sc_width, sc_height]) #screen size 


start_menu = True
game_interface = False

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):

        screen.blit(self.image, self.rect)

#Buttons-Sprites
start_img = pg.image.load('assets//others//play.png')
options_img = pg.image.load('assets//others//options.png')
credits_img = pg.image.load('assets//others//credits.png')

#Creating/to screen/coords
start_button = Button(x_center(sc_width, start_img.get_width()), 330, start_img)
options_button = Button(x_center(sc_width, options_img.get_width()), 450, options_img)
credits_button = Button(x_center(sc_width, credits_img.get_width()), 570, credits_img)

#this is the loop we'll code inside
running = True
while running:
    clock.tick(60)#DO NOT REMOVE THIS 

    screen.fill((0, 0, 0))

    #Menu    
    if start_menu == True:
        start_button.draw()
        options_button.draw()
        credits_button.draw()
    else:
        pass

        
#EventPanel
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False #quits the pygame window when we click on X 

        #detects click on sprite 
        if pg.mouse.get_pressed()[0] and start_button.rect.collidepoint(pg.mouse.get_pos()) and not handled: 
            game_interface = True
        handled = pg.mouse.get_pressed()[0]

        if game_interface == True:
            start_menu = False
            screen.fill((0, 0, 0))

        if event.type == pg.MOUSEBUTTONDOWN:
            print('code works')


    pg.display.flip()