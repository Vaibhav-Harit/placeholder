import pygame as pg
from functions import *
import time

pg.init()


#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
sc_width = 640
sc_height = 640
screen = pg.display.set_mode([sc_width, sc_height], pg.RESIZABLE)
display = pg.Surface((sc_width,sc_height)) # used as the surface for rendering, which is scaled




def multlines(text, configs, fontsize):
    text = text.splitlines()
    for i, j in enumerate(text):
        screen.blit(configs.render(j, True, (255, 0, 0)), (0, fontsize*i))





# Title/Icon (Nothing is Decided)
pg.display.set_caption("PLACEHOLDER")


# Player
vel = 5
char_sprite = pg.image.load('assets//characters//Character_sprite_placeholder.png')
char_sprite = pg.transform.scale(char_sprite, (32, 64)) # setting character dimensions
test_player = Player(sprite = char_sprite, screen_wh = (sc_width, sc_height), health = 1000, luck = 1000, power = 10 ,speed = 10, defense = 10)

# Map
map_machine = map_renderer(map_dir = 'assets//maps//test1.tmx', tile_dir = 'assets//tiles', render_position = (0, 0), tile_length = 64, screen_wh = (sc_width, sc_height), map_user = test_player)
test_player.map = map_machine
# test_player.x = 4500
# test_player.y = 700
# Game loop
running = True
while running:
    print(clock.tick(60)) # DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    #Key Presses
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        test_player.update_position(-vel, 0)

    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        test_player.update_position(vel, 0)

    if keys[pg.K_UP] or keys[pg.K_w]:
        test_player.update_position(0, -vel)

    if keys[pg.K_DOWN] or keys[pg.K_s]:
        test_player.update_position(0, vel)



    screen.fill((255, 255, 255)) # screen color RGB

    map_machine.render(screen)
    test_player.render(screen)
    # multlines(f'True_Scroll : {scroll}\nPlayer_Coords : {[test_player.x -384, test_player.y -268]}', pg.font.Font('freesansbold.ttf',25), 25) # add this before display.update if u wanna see the x, y pos of the square
    pg.display.update()