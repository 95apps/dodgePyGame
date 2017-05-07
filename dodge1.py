"""
Brendan Wu
May 6 2017
Submitted to ICS 3U1 - Mr. Cope

dodge.py - an arcade survival game

Version 1 : Barebones
Basic framework taken from program files with an added player,player controls and boundaries.
Stripped R, G, B functions.

"""

import pygame
from pygame.locals import *
pygame.init()

size = (400, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Yeah, Pygame!")


background = pygame.Surface(size)
background = background.convert()
background.fill((255, 255, 255))

clock = pygame.time.Clock()
keep_going = True

sprite = pygame.image.load("ball.bmp")
sprite_rect = sprite.get_rect()
sprite_rect.centerx = (size[0]//2)
sprite_rect.centery = (size[1] - 50)



while keep_going:

    clock.tick(120)

    keyinput = pygame.key.get_pressed()

    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        elif ev.type == KEYDOWN:
            if ev.key == K_r:
                print("r")

    if keyinput[pygame.K_LEFT] and sprite_rect.centerx > 0:
        sprite_rect.centerx -= 10
    elif keyinput[pygame.K_RIGHT] and sprite_rect.centerx < size[0]:
        sprite_rect.centerx += 10


    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_rect)
    pygame.display.flip()