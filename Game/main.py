"""Main file for asteroid game."""
from sys import exit as sys_exit
import pygame
from ShipFile import Ship
from AsteroidFile import Asteroid
pygame.init()

size = width, height = 1000, 570

window = pygame.display.set_mode(size)
c = pygame.time.Clock()

# Load the ship object
ship = Ship()

# Load asteroid
asteroid = Asteroid()

# Load background
bg = pygame.image.load('./image/spacebg.jpeg')
all_sprites = pygame.sprite.Group(ship, asteroid)

# Rescale bg to window size and rescale asteroid
bg = pygame.transform.scale(bg, size)

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys_exit()

    # Load images and update ship and asteroid
    window.blit(bg, (0, 0))
    ship.update(asteroid)
    asteroid.update()

    ship.draw(window)
    asteroid.draw(window)

    # Check the boundaries
    if ship.y > height - ship.height:
        ship.y = height - ship.height
    if ship.y < 0:
        ship.y = 0

    pygame.display.update()
    c.tick(60)
    pygame.display.flip()
