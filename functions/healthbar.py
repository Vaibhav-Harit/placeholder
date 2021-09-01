import pygame as pg


pg.init()
#setting up the basics cuz these nubs no read tutorial
clock = pg.time.Clock()
screen = pg.display.set_mode([800, 700])

# Title/Icon (Nothing is Decided)
pg.display.set_caption("NOT DECIDED")
   #icon later

#Player
charac_sprite = pg.image.load('assets//characters//Character_sprite_placeholder.png')

#Health Bar
staminabar_sprite = pg.image.load('assets//player_ui//Staminabar.png')
healthbar_sprite = pg.image.load('assets//player_ui//Healthbar.png')
healthbaroverlay_sprite = pg.image.load('assets//player_ui//Healthbar_overlay.png')

maxHp = 100
hp = 100
maxSt = 100
st = 100
stRegenAcceleration = 0
displayHp = 100 #Will gradually catch up with HP to create a smooth effect when you lose health
displaySt = 100

#def
def player():
    screen.blit(charac_sprite, ((1350, 700)))
#def
def bars():
    screen.blit(healthbar_sprite, (((1-displayHp/maxHp)*-171, 0)))#171 is width of Health bar
    screen.blit(staminabar_sprite, (((1-displaySt/maxSt)*-160, 0)))#160 is width of Stamina bar
    screen.blit(healthbaroverlay_sprite, ((0, 0)))
    


#Game loop
running = True
while running:
    clock.tick(60) #DO NOT REMOVE
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    
    if pg.key.get_pressed()[pg.K_SPACE] and hp > 0:
        hp -= 1
    if pg.key.get_pressed()[pg.K_w] and st > 0:
        st -= 1
        stRegenAcceleration = 0
    else:
        if maxSt > st:
            st += stRegenAcceleration
            stRegenAcceleration += 0.01
        else:
            stRegenAcceleration = 0
            st = maxSt
    displayHp += (hp - displayHp)/10#change '10' to larger value to make the effect smoother or the opposite for more isntant
    displaySt += (st - displaySt)/10
    if hp > maxHp:
        hp = maxHp


    screen.fill((0, 0, 0)) #screen color RGB

    player()
    bars()
    pg.display.update()