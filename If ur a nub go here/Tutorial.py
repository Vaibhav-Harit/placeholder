#JUST
#FOR
#REFFERENCE

#NOT
#THE
#GAME
#CODE



import pygame as pg

# im not gonna explain this
def multlines(text, configs, fontsize):
    text = text.splitlines()
    for i, j in enumerate(text):
        screen.blit(configs.render(j, True, (255, 0, 0)), (0, fontsize*i))


pg.init() # initializing pygame - basically starting it up

# setting clock
clock = pg.time.Clock() 
screen = pg.display.set_mode([500, 500]) # this sets the height and width of the pygame window
square = pg.Surface((20, 20)) # this is a square thats gonna move around we can use our sprites later
square.fill((255, 255, 255)) # filling it with RGB color values, where R, G, G = 255, 255, 255 (mess aound with the colors if u want)
rect = square.get_rect() # This is an object that will determine the position of our square rect.x, rect.y will return the corresponding x and y values

'''
This is the while loop or our GAME LOOP
In this loop we are gonna code commands for what happens in each frame

Note: One frame is over after one pass in the loop

Somethings you should know about pygame:

    -Pygame works on a grid based system,so like coordinates X, Y, well be using this alot to determine postions of stuff
        -In this grid system the coords (0,0) are located at the top left of the pygame window
    -We need to draw or 'blit' stuff on the screen for each frame, in esscence like the process of making a hand drawn 2d animation
'''
while True: 
    clock.tick(60) # This is the time delay for each frame, its set to 60 milisecs here, if you remove this delay ur pc gonna heaet up lol
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    pressed = pg.key.get_pressed() # This will send us a list of truth values these values are corresponding to the keys being pressed in you keyboard
    # if a key is pressed it will return true, you can try printing pressed to see what it looks like
    if pressed[pg.K_UP]:# As i mentioned above pressed is just a list of True and falses(or 1s and 0s) pg.K_<name> is an variable that already exists in
        # the pygame library, pg.K_<name> where K_ means key and <name> is the name of the key is just number which represents the index of the key being
        # pressed in the list
        rect.y -= 1
    if pressed[pg.K_DOWN]:
        rect.y += 1
    if pressed[pg.K_LEFT]:
        rect.x -= 1
    if pressed[pg.K_RIGHT]:
        rect.x += 1

    screen.fill((0, 0, 0)) # background (uses RGB)
    screen.blit(square, rect)# the first arguement (square, which you can see we made above) contains info on the image we are about to draw
    # ,which is a white square, the second arguement rect is the position in which we are going to draw said square
    pg.display.update()# updates the frame



multlines(f'X :   {rect.x}\nY :  {rect.y}\n', pg.font.Font('freesansbold.ttf',25), 25) # add this before display.update if u wanna see the x, y pos of the square