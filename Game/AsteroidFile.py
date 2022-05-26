import pygame
import random
pygame.init()

class asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/Nasminkaisar/PycharmProjects/AyaanZ1/Game/image/asteroid.png')
        self.x = random.randint(0,1018)
        self.y = random.randint(0,573)
        self.width,self.height = self.image.get_size()
        self.rect = self.image.get_rect()
        #make the asteroid 1/2 of its size

    def move(self):
        self.x -= 5

    def update(self):
        self.move()
        if self.y > 573:
            self.y = 0
        if self.y < 0:
            self.y = 573
        if self.x > 1018:
            self.x = 0
            self.y = random.randint(0,573)
        if self.x < 0:
            self.x = 1018
            self.y = random.randint(0+self.height,573-self.height)