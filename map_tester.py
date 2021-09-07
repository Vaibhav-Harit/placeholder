import pygame as pg
from functions import *

pg.init()

#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
sc_width = 800
sc_height = 600
screen = pg.display.set_mode([sc_width, sc_height], pg.RESIZABLE)

def multlines(text, configs, fontsize):
    text = text.splitlines()
    for i, j in enumerate(text):
        screen.blit(configs.render(j, True, (255, 0, 0)), (0, fontsize*i))





# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED")

# Player
char_sprite = pg.image.load('assets//characters//Character_sprite_placeholder.png')
char_sprite = pg.transform.scale(char_sprite, (32, 64)) # setting character dimensions
test_player = Player(char_sprite, (sc_width, sc_height), 1000, 1000, 10 ,10, 10)
vel = 1

# Map
map_machine = map_renderer('assets//maps//test1.tmx', 'assets//tiles', (0, 0), 32, (sc_width, sc_height))

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
        # test_player.update_position(-1 * vel, 0)
        map_machine.move_map(vel, 0)
    if keys[pg.K_RIGHT]:
        # test_player.update_position(vel, 0)
        map_machine.move_map(-vel, 0)
    if keys[pg.K_UP]:
        # test_player.update_position(0, -1 * vel)
        map_machine.move_map(0, vel)

    if keys[pg.K_DOWN]:
        # test_player.update_position(0, vel)
        map_machine.move_map(0, -vel)



    screen.fill((255, 255, 255)) # screen color RGB
    map_machine.render(screen)
    test_player.render(screen)
    multlines(f'X :   {map_machine.x}\nY :  {map_machine.y}\n', pg.font.Font('freesansbold.ttf',25), 25) # add this before display.update if u wanna see the x, y pos of the square
    pg.display.update()