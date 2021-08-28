import pygame as pg
from functions import *

pg.init()

#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
sc_width = 600
sc_height = 600
screen = pg.display.set_mode([sc_width, sc_height])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED")

#Player
charac_sprite = pg.image.load('assets//Character_sprite_placeholder.png')
test_player = Player(charac_sprite, (sc_width, sc_height), 10, 10, 10)


#Game loop
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    
    #Key Presses
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x -= vel        
    if keys[pg.K_RIGHT]:
        x += vel
    if keys[pg.K_UP]:
        y -= vel
    if keys[pg.K_DOWN]:    
        y += vel


    screen.fill((0, 0, 0)) #screen color RGB

    test_player.render(screen)
    pg.display.update()