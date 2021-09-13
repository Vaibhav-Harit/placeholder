import pygame as pg
from functions import *
import time

pg.init()


#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
sc_width = 800
sc_height = 600
screen = pg.display.set_mode([sc_width, sc_height], pg.RESIZABLE)
display = pg.Surface((sc_width,sc_height)) # used as the surface for rendering, which is scaled




def multlines(text, configs, fontsize):
    text = text.splitlines()
    for i, j in enumerate(text):
        screen.blit(configs.render(j, True, (255, 0, 0)), (0, fontsize*i))





# Title/Icon (Nothing is Decided)
pg.display.set_caption("PLACEHOLDER")


# Player
char_sprite = pg.image.load('assets//characters//Character_sprite_placeholder.png')
char_sprite = pg.transform.scale(char_sprite, (32, 64)) # setting character dimensions
test_player = Player(char_sprite, (sc_width, sc_height), 1000, 1000, 10 ,10, 10)
center_x = test_player.x
center_y = test_player.y
print((center_x, center_y))
vel = 5

# Map
map_machine = map_renderer('assets//maps//test1.tmx', 'assets//tiles', (0, 0), 64, (sc_width, sc_height))

# Game loop
running = True
while running:
    map_machine.true_scroll[0] += (test_player.x - map_machine.true_scroll[0] - center_x)//20
    map_machine.true_scroll[1] += (test_player.y - map_machine.true_scroll[1] - center_y)//20
    scroll = map_machine.true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])


    clock.tick(60) # DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    #Key Presses
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        test_player.update_position(-vel, 0)

    if keys[pg.K_RIGHT]:
        test_player.update_position(vel, 0)

    if keys[pg.K_UP]:
        test_player.update_position(0, -vel)

    if keys[pg.K_DOWN]:
        test_player.update_position(0, vel)



    screen.fill((255, 255, 255)) # screen color RGB

    map_machine.render(screen, scroll[0], scroll[1])
    test_player.render(screen, scroll[0], scroll[1])
    # multlines(f'True_Scroll : {scroll}\nPlayer_Coords : {[test_player.x -384, test_player.y -268]}', pg.font.Font('freesansbold.ttf',25), 25) # add this before display.update if u wanna see the x, y pos of the square
    pg.display.update()