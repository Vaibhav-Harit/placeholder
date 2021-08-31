import pygame as pg
from functions.Helper_Functions import *
import random

class Monster(object):
    #initialization
    def __init__(self, name: str, sprite, position: tuple, health, attack, defense, speed):
        self.name = name
        self.sprite = sprite
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

        self.x = position[0]
        self.y = position[1]

    def render(self, screen: pg.display):
        screen.blit(self.sprite, (self.x, self.y))

    def move(self, velocity, player_near = False, player_position = None):
        #if the player is not within range
        if player_near == False:
            movement_type = random.randint(1, 4)
            if movement_type == 1:  #moving right
                self.x += velocity
            elif movement_type == 2:    #moving left
                self.x -= velocity
            elif movement_type == 3:  #moving down
                self.y += velocity
            elif movement_type == 4:    #moving up
                self.y -= velocity
            
        #if the player is within range
        if player_near == True:
            player_x = player_position[0]
            player_y = player_position[1]

            if player_x > self.x:
                self.x += velocity
            elif player_x < self.x:
                self.x -= velocity
            
            if player_y > self.y:
                self.y += velocity
            elif player_y < self.y:
                self.y -= velocity
            

    def combat(self):
        pass

            







