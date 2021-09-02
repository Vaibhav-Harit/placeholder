from functions.Monster_Object import *
import pygame as pg
from functions import *

pg.init()

#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
sc_width = 800
sc_height = 600
screen = pg.display.set_mode([sc_width, sc_height])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("monster testing")

#Player Sprites
char_sprite = pg.image.load('assets//characters//Character_sprite_placeholder.png')
char_sprite = pg.transform.scale(char_sprite, (32, 64))
test_player = Player(char_sprite, (sc_width, sc_height), 1000, 1000, 10 ,10, 10)
test_monster = Monster("testmonstah", char_sprite, (100, 100), 10, 10, 10, 10)

#making an event for enemies
enemy_move = pg.USEREVENT + 1

#setting the timer
pg.time.set_timer(enemy_move, 100)

#Movement speed
vel = 5
enemy_steps = 5
enemy_range = 200

#Game loop
running = True
while running:
    clock.tick(60) #DO NOT REMOVE         
#Event Panel    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        #delays enemy movement
        if event.type == enemy_move:
            if abs(test_player.x - test_monster.x) <= enemy_range and abs(test_player.y - test_monster.y) <= enemy_range:
                test_monster.move(vel, True, (test_player.x, test_player.y))
            else:
                test_monster.move(vel, False, None)
            

    #Key Presses
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        if test_player.x > 0:
            test_player.update_position(-1 * vel, 0)
    if keys[pg.K_RIGHT]:
        if test_player.x < (sc_width - test_player.char_width):
            test_player.update_position(vel, 0)
    if keys[pg.K_UP]:
        if test_player.y > 0:
            test_player.update_position(0, -1 * vel)
    if keys[pg.K_DOWN]:
        if test_player.y < (sc_height - test_player.char_height): 
            test_player.update_position(0, vel)

    #checks player distance to monster
    
    

    screen.fill((255, 255, 255)) #screen color RGB
    test_player.render(screen)
    test_monster.render(screen)
    pg.display.update()
   