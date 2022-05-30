"""File with the Asteroid class"""
from random import randint
import pygame
pygame.init()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize the asteroid"""
        super().__init__()
        self.image = pygame.image.load('./image/asteroid.png')
        self.image.convert_alpha()
        self.x = 1018
        self.y = randint(0, 573)
        self.width, self.height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.width // 2, self.height // 2))
        self.rect = self.image.get_rect()  # topleft=(1018, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """Move the asteroid"""
        self.x -= 5
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Update the asteroid"""
        self.move()
        if self.y > 573:
            self.y = 0
        elif self.y < 0:
            self.y = 573

        if self.x > 1018:
            self.x = 0
            self.y = randint(0, 573)
        elif self.x < 0:
            self.x = 1018
            self.y = randint(self.height, 573 - self.height)

    def draw(self, screen):
        """Draw the asteroid"""
        screen.blit(self.image, (self.x, self.y))
        print(self.rect)
