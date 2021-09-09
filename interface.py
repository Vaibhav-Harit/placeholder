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


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, self.rect)

    def clicked(self):
        if pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos()):
            return True
        else:
            return False
    


#Sprites
imgload = pg.image.load
rescale = pg.transform.scale

start_img = rescale(imgload('assets//interface//play.png'), (200, 60))
# attack_img = rescale(imgload('assets//interface//'), (w, h))
skill_frame_img = rescale(imgload('assets//interface//player_ui//skillframe.png'), (100, 100))
healthbar_img = rescale(imgload('assets//interface//player_ui//healthbar.png'), (100, 100))
# level_frame_img = rescale(imgload('assets//interface//')), (w, h))
# level1_img = rescale(imgload('assets//interface), (w,h))


options_img = rescale(imgload('assets//interface//options.png'), (200, 60))
musicon_img = rescale(imgload('assets//interface//music on.png'), (100, 100))
musicoff_img = rescale(imgload('assets//interface//music off.png'), (100, 100))


credits_img = rescale(imgload('assets//interface//credits.png'), (200, 60))




#Button Instances
start_button = Button(x_center(sc_width, start_img.get_width()), 400, start_img)
# attack_button = Button(1000, 500, attack_img)
skill_frame_button1 = Button(900, 400, skill_frame_img)
skill_frame_button2 = Button(1000, 450, skill_frame_img)
skill_frame_button3 = Button(1100, 500, skill_frame_img)
healthbar_button = Button(300, 300, healthbar_img)

options_button = Button(x_center(sc_width, options_img.get_width()), 470, options_img)
musicon_button = Button(10, 100, musicon_img)
musicoff_button = Button(x_center(sc_width, musicon_img.get_width()), 200, musicoff_img)

credits_button = Button(x_center(sc_width, credits_img.get_width()), 540, credits_img)






#Boolians
start_menu = True
game_interface = False
options_menu = False
credits_menu = False
inventory_menu = False


#Variables
MUSIC = bool
PLAYING = bool

#MAIN LOOP
running = True
while running:
    clock.tick(60)#DO NOT REMOVE THIS 



#EventPanel

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False #quits the pygame window when we click on X 



    #ALL CLICK DETECTIONS HERE    

        if start_button.clicked(): 
            screen.fill((0, 0, 0))
            game_interface = True
            start_menu = False
            
        
        if options_button.clicked():
            screen.fill((0, 0, 0))
            start_menu = False
            options_menu = True

        if credits_button.clicked():
            pass # lol we're not even sure if we want this

        if musicon_button.clicked():
            screen.fill((0, 0, 0))
            musicoff_button.draw()

        if musicoff_button.clicked():
            screen.fill((0, 0, 0))
            musicon_button.draw()

        

    #ALL INTERFACE CONVERSIONS AND SPRITE BLITTING HERE

        if start_menu == True:
            start_button.draw()
            options_button.draw()
            credits_button.draw()
            
            start_menu = False
        
        
        if game_interface == True:
            #attack_button.draw()
            skill_frame_button1.draw()
            skill_frame_button2.draw()
            skill_frame_button3.draw()
            healthbar_button.draw()

            PLAYING = True
            game_interface = False


        if options_menu == True:
            if MUSIC == True:
                musicon_button.draw()
            else:
                musicoff_button.draw()

            options_menu = False





    pg.display.flip()