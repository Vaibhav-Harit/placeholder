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

        self.initial_position = position
        self.x = position[0]
        self.y = position[1]

    def render(self, screen: pg.display):
        screen.blit(self.sprite, (self.x, self.y))
    
    #picks a random destination within range
    def destination(self, range):
        current_position = (self.x, self.y)
        #checks if the monster is beyond permissible range for wandering(-10 for allowance)
        if distance(self.initial_position, current_position) >= range - 10:
            set_destination = self.initial_position
        else:
            random_x = random.randint(-1 * (range), range)
            random_y = random.randint(-1 * (range), range)
            set_destination = ((self.x + random_x), (self.y + random_y))
        
        return set_destination

    #movement when player in not nearby
    def wander(self, velocity, target: tuple):
        target_coords_x = target[0]
        target_coords_y = target[1]

        if abs(target_coords_x - self.x) > velocity:
            if self.x < target_coords_x: #moving right
                self.x += velocity
            elif self.x > target_coords_x: #moving left
                self.x -= velocity
        if abs(target_coords_y - self.y) > velocity:
            if self.y < target_coords_y: #moving down
                self.y += velocity
            elif self.y > target_coords_y: #moving up
                self.y -= velocity


    #movement to chase the player if it is within range
    def chase(self, velocity, player_position: tuple):
        player_x = player_position[0]
        player_y = player_position[1]

        if abs(player_x - self.x) > velocity:
            if player_x > self.x:
                self.x += velocity
            elif player_x < self.x:
                self.x -= velocity

        if abs(player_y - self.y) > velocity:    
            if player_y > self.y:
                self.y += velocity
            elif player_y < self.y:
                self.y -= velocity


    def combat(self):
        pass

            







