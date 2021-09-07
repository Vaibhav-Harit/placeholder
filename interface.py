import pygame as pg
import random
import math
import assets
from functions.Helper_Functions import *


pg.init()



#setting up the pygame window
clock=pg.time.Clock()
sc_width = 1300
sc_height = 700
screen = pg.display.set_mode([sc_width, sc_height]) #screen size 


start_menu = True
game_interface = False
options_menu = False

class Button:
    def __init__(self, x, y, image):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, self.rect)

    def clicked(self):
        pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos()) and not pg.mouse.get_pressed()[0]

            
#Button Sprites
imgload = pg.image.load

start_img = imgload('assets//interface//play.png')
options_img = imgload('assets//interface//options.png')
credits_img = imgload('assets//interface//credits.png')
attack_img = imgload('assets//interface//attack.png')
musicon_img = imgload('assets//interface//music on.png')
musicoff_img = imgload('assets//interface//music off.png')



#Creating/to screen/coords
start_button = Button('start', x_center(sc_width, start_img.get_width()), 330, start_img)
options_button = Button('options', x_center(sc_width, options_img.get_width()), 450, options_img)
credits_button = Button('credits', x_center(sc_width, credits_img.get_width()), 570, credits_img)
attack_button = Button('attack', 350, 350, attack_img)


#MAIN LOOP
running = True
while running:
    clock.tick(60)#DO NOT REMOVE THIS 

    #Menu

        
#EventPanel
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False #quits the pygame window when we click on X 

        if start_menu == True:
            screen.fill((0, 0, 0))
            start_button.draw()
            options_button.draw()
            credits_button.draw()

    #ALL CLICK DETECTIONS HERE    
        #start button
        if start_button.clicked(): 
            screen.fill(0, 0, 0)
            game_interface = True
            start_menu = False
            print('mmmmmmmm')
        
        if pg.mouse.get_pressed()[0] and options_button.rect.collidepoint(pg.mouse.get_pos()) and not handled:
            start_menu = False
            options_menu = True



    #ALL INTERFACE CONVERSIONS AND SPRITE BLITTING HERE
        if game_interface == True:
            screen.fill((0, 0, 0))
            print ('.')
            


        if options_menu == True:
            pass


    pg.display.flip()