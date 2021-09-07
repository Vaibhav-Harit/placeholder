import pygame as pg 
from functions.Helper_Functions import *


class Player(object):
    #initialization, will automatically run when you do a new instance
    def __init__(self, sprite : pg.image, screen_wh : tuple, health : int, luck : int,  pwr : int, spd : int, defense : int):
        #basic stats
        self.power = pwr
        self.speed = spd
        self.defense = defense
        # setting up health bar
        health_assets = [pg.image.load('assets//interface//player_ui//Healthbar_overlay.png'), pg.image.load('assets//interface//player_ui//Healthbar.png'), pg.image.load('assets//interface//player_ui//Staminabar.png')]
        self.health_bar = Health_Bar(health_assets, health, luck, .2) 
        
        #sprite, height and width
        self.sprite = sprite
        self.char_width = sprite.get_width()
        self.char_height = sprite.get_height()

        #position handling
        positon = center_coords(screen_wh, (sprite.get_width(), sprite.get_height()))
        self.x = positon[0]
        self.y = positon[1]

    def render(self, screen : pg.display):
        screen.blit(self.sprite, (self.x, self.y))
        self.health_bar.render_bars(screen)

    def attack(self, ):
        pass

    def update_position(self, x_diff, y_diff):
        if x_diff >= 0:
            self.x += x_diff
        elif x_diff < 0:
            self.x -= abs(x_diff)

        if y_diff >= 0:
            self.y += y_diff
        elif y_diff < 0:
            self.y -= abs(y_diff)

    def sprint(self, ):
        pass

    def move(self, ):
        pass

    def block(self, ):
        pass

    def pick_up(self, ):
        pass

    def activate_skill(self, ):
        pass

class Health_Bar():
    def __init__(self, sprites : list, maxHP : int, maxL : int, recovery_rate : int):
        self.maxHP = maxHP
        self.hp = maxHP
        self.display_hp = maxHP #Will gradually catch up with HP to create a smooth effect when you lose health
        self.maxL = maxL
        self.luck = maxL
        self.display_luck = maxL
        self.recovery = 0
        self.recovery_rate = recovery_rate
        self.overlay = sprites[0]
        self.health_bar = sprites[1]
        self.h_width = self.health_bar.get_width()
        self.luck_bar  = sprites[2]
        self.l_width = self.luck_bar.get_width()
        
    def render_bars(self, screen : pg.display):
        if self.maxL > self.luck:
            self.luck += self.recovery
            self.recovery += self.recovery_rate
        else:
            self.recovery = 0
            self.luck = self.maxL
        if self.hp > self.maxHP:
            self.hp = self.maxHp

        self.display_hp += (self.hp - self.display_hp)/10 #c hange '10' to larger value to make the effect smoother or the opposite for more isntant
        self.display_luck += (self.luck - self.display_luck)/10

        screen.blit(self.health_bar, (((1 - self.display_hp/self.maxHP)* - (self.h_width), 0)))
        screen.blit(self.luck_bar, (((1 - self.display_luck/self.maxL) * - (self.l_width), 0)))
        screen.blit(self.overlay, ((0, 0)))

    def update_vals(self, hp_diff : int = 0, l_diff : int = 0):
        if self.hp > 0:
            self.hp += hp_diff
        if self.luck > 0:
            self.luck += l_diff
            self.recovery = 0





class Weapon(object):
    def __init__(self, sprite : pg.image, screen_wh : tuple, pwr : int, spd : int,):
        self.power = pwr
        self.speed = spd
        self.sprite = sprite
