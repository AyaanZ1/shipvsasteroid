import pygame

from Game.main import window

pygame.init()

class ship(pygame.sprite.Sprite):
    def __init__(self, window):
        super.__init__()
        self.image = pygame.image.load('ship.png')
        self.x = 254
        self.y = 286

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 10
        if keys[pygame.K_DOWN]:
            self.y += 10

    def draw(self):
        window.blit(self.image,(self.x,self.y))
    def update(self):
        self.move()
        self.draw()