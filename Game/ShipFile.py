import pygame
import sys
pygame.init()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.image = pygame.image.load('./image/ship.png')
        self.image.convert_alpha()
        self.x = 255
        self.y = 290
        self.width, self.height = self.image.get_size()
        self.rect = self.image.get_rect()#topleft=(254, 286))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, obstacle):
        """Update the ship's position based on the currently pressed keys."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 10
        if keys[pygame.K_DOWN]:
            self.y += 10
        self.rect.x = self.x
        self.rect.y = self.y

        #if pygame.sprite.spritecollide(self, pygame.sprite.GroupSingle(obstacle), False, pygame.sprite.collide_mask):
        #    print("Game Over")
        #    sys.exit()
        if pygame.sprite.collide_mask(self, obstacle):
            print("Game Over")
            sys.exit()

    def draw(self, screen):
        """Draw the ship on the screen."""
        screen.blit(self.image, self.rect)
