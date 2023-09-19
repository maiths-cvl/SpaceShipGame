import pygame
from spaceship import *
from planet import *
from projectile import *

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Spaceship Game")
font = pygame.font.Font('freesansbold.ttf', 32)

Player = Spaceship()
planett = Planet()
missile = Projectile()

fps = 60
clock = pygame.time.Clock()

spacepressed = False
throw = False

points = 0




run = True
while run:

    text = font.render(str(points), True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (30, 15)

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    screen.fill((0, 0, 0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        Player.pos[0] -= Player.speed
    elif pressed[pygame.K_d]:
        Player.pos[0] += Player.speed
    elif pressed[pygame.K_SPACE]:
        if spacepressed == False:
            print('player shoot !!!!')
            throw = True
            missile.loc = Player.pos.copy()
            spacepressed = True
    if pressed[pygame.K_SPACE] == False:
        spacepressed = False


    print((missile.loc[1]/5), int(planett.loc[1]/5), int(missile.loc[0]/planett.size), int(planett.loc[0]/planett.size))
    if ((missile.loc[1]/5) == int(planett.loc[1]/5) and int(missile.loc[0]/planett.size) == int(planett.loc[0]/planett.size)):
        missile.destroyState == True
        throw = False
        missile.loc = [-100, -100]
        #missile.update()
        planett.destroys()
        points += 1

    if throw:
        missile.update()

    screen.blit(text, textRect)
    pygame.draw.circle(screen, (255, 255, 255), missile.loc, 5)
    screen.blit(Player.img, Player.pos)
    pygame.draw.circle(screen, (0, 155, 12), planett.loc, planett.size)
    

    

    pygame.display.update()
