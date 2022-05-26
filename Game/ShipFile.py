import pygame



pygame.init()

class ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./image/ship.png')
        self.x = 254
        self.y = 286
        self.width,self.height = self.image.get_size()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 10
        if keys[pygame.K_DOWN]:
            self.y += 10

    def update(self):
        self.move()