import pygame as pg
import time
from functions import * 

clock = pg.time.Clock()
sc_width = 800
sc_height = 600
screen = pg.display.set_mode([sc_width, sc_height])

def dialog(message):
    global letters_shown
    global time_passed
    letter_x = 50
    letter_num = 0
    letter_y = 50
    letter_num = 0
    i = 0
    j = 0
    initial_letter_x = 0
    words = message.split()
    
    m = len(words)
    while (j < m):
        n = len(words[j])
        i = 0
        
        word_pixel_length = 0
        while (i < n):
            letter = words[j][i]
            
            if letter == '.':
                word_pixel_length += 6
            elif letter == 'm':
                word_pixel_length += 18
            elif letter == 'w':
                word_pixel_length += 18
            elif letter == ',':
                word_pixel_length += 6
            elif letter == '"':
                word_pixel_length += 10
            elif letter == '!':
                word_pixel_length += 6
            else:
                word_pixel_length += 14
            i += 1
        i = 0
        while (i < n):
            
            letter = words[j][i]
            if word_pixel_length + initial_letter_x > 600:
                letter_y += 30
                letter_x = 50
                initial_letter_x = 0

            if not letter == ' ':
                if letter == '.':
                    path = 'assets//font//dot.png'
                elif letter == '?':
                    path = 'assets//font//!2.png'
                elif letter == '"':
                    path = 'assets//font//speech_marks.png'
                else:
                    path = f'assets//font//{letter}.png'
                if letters_shown >= letter_num:
                    screen.blit(pg.image.load(path), (letter_x, letter_y))
            
            if letter == '.':
                letter_x += 6
            elif letter == 'm':
                letter_x += 18
            elif letter == 'w':
                letter_x += 18
            elif letter == ',':
                letter_x += 6
            elif letter == '"':
                letter_x += 10
            elif letter == '!':
                letter_x += 6
            else:
                letter_x += 14
            i += 1
            letter_num += 1    
             


        initial_letter_x = letter_x
        j += 1
        letter_x += 14
        
    return;

running = True
start_time = time.time()
while running:
    clock.tick(60) #DO NOT REMOVE         
#Event Panel    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    screen.fill((0, 0, 0)) #screen color RGB
    dialog('A wizard beckons, "come forth young one", you hesitate, not knowing what will happen if you decline his malicious offer...')


    pg.display.update()