import pygame
import sys
import random

pygame.init()

w = 1018
h = 573

window = pygame.display.set_mode((w,h))
c = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #load images
    bg = pygame.image.load('bg.png')
    window.blit(bg,(0,0))
