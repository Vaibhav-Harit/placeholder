import pygame as pg


pg.init()
#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
screen = pg.display.set_mode([800, 700])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED")




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


#Health Bar
staminabar_sprite = pg.image.load('assets//player_ui//Staminabar.png')
healthbar_sprite = pg.image.load('assets//player_ui//Healthbar.png')
healthbaroverlay_sprite = pg.image.load('assets//player_ui//Healthbar_overlay.png')

maxHp = 100
maxSt = 100


helth = Health_Bar([healthbaroverlay_sprite, healthbar_sprite, staminabar_sprite], maxHp, maxSt, .2)



#Game loop
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    
    if pg.key.get_pressed()[pg.K_SPACE]:
        helth.update_vals(-1)
    if pg.key.get_pressed()[pg.K_w]:
        helth.update_vals(0, -1)

    screen.fill((0, 0, 0)) #screen color RGB
    helth.render_bars(screen)
    pg.display.update()