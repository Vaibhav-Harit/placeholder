import pygame as pg
from functions import *

pg.init()

#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
sc_width = 700
sc_height = 700
screen = pg.display.set_mode([sc_width, sc_height])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED")

# Player
char_sprite = pg.image.load('assets//Character_sprite_placeholder.png')

test_player = Player(char_sprite, (sc_width, sc_height), 10, 10, 10)
vel = 5

# Map
map_set = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
map_set = map_organizer(map_set, 20, 30)
wood_floor = pg.image.load('assets//tiles//Wood floor.png')
wood_roof = pg.image.load('assets//tiles//Wood roof.png')
tile_set = [wood_floor, wood_roof]

map_machine = map_renderer(map_set, tile_set, (0, 0))


# Game loop
running = True
while running:
    clock.tick(60) # DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    

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

    screen.fill((0, 0, 0)) # screen color RGB
    map_machine.render(screen)
    test_player.render(screen)
    pg.display.update()