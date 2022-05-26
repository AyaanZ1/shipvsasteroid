import pygame
import sys
import random
from ShipFile import ship
from AsteroidFile import asteroid

pygame.init()

w = 1018
h = 573

window = pygame.display.set_mode((w,h))
c = pygame.time.Clock()
#load the ship object
ship = ship()
asteroid = asteroid()
bg = pygame.image.load('/Users/Nasminkaisar/PycharmProjects/AyaanZ1/Game/image/spacebg.jpeg')
#rescale bg to window size and rescale asteroid
bg = pygame.transform.scale(bg,(w,h))
pygame.time.wait(100)
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #load images and update ship and asteroid

    window.blit(bg,(0,0))
    ship.update()
    window.blit(ship.image,(ship.x,ship.y))
    window.blit(asteroid.image, (asteroid.x, asteroid.y))
    asteroid.update()

    #check the boundaries

    if ship.y > h - ship.height:
        ship.y = h - ship.height
    if ship.y < 0:
        ship.y = 0
    #check for collision with a pygame collision detection function
    if pygame.sprite.collide_rect(ship, asteroid) and c.get_time() > 1000:
        #display game over
        text = pygame.font.Font('freesansbold.ttf', 32)
        textSurf = text.render('KO', True, (255,0,0))
        textRect = textSurf.get_rect()
        sys.exit()

    pygame.display.update()
    c.tick(60)
    pygame.display.flip()