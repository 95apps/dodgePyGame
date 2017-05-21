"""
Brendan Wu
May 6 2017
Submitted to ICS 3U1 - Mr. Cope

dodge.py - an arcade survival game

Version 2 : Typing
This version allows users to type and delete characters onto the screen. Characters are saved in a string
that can be used later to blast asteroids.

"""

import pygame
from pygame.locals import *

pygame.init()

myfont = pygame.font.SysFont("Arial", 15)
label = myfont.render("Some text!", 1, (123,131,0))


size = (400, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Yeah, Pygame!")

background = pygame.Surface(size)
background = background.convert()
background.fill((255, 255, 255))
screen.blit(background, (0, 0))

clock = pygame.time.Clock()
keep_going = True

sprite = pygame.image.load("ball.bmp")
sprite_rect = sprite.get_rect()
sprite_rect.centerx = (size[0] // 2)
sprite_rect.centery = (size[1] - 50)

text = ""

def type(text):
   screen.blit(background, (0,0))
   font=pygame.font.SysFont("Arial",30)
   typetext=font.render(text, 1,(0,0,0))
   screen.blit(typetext, (size[0] //2, size[1] - 150))


while keep_going:

    clock.tick(1000)
    print(text)
    keyinput = pygame.key.get_pressed()


    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        elif ev.type == KEYDOWN:
            if ev.key == K_a:
                text += "a"
                type(text)
            elif ev.key == K_b:
                text += "b"
                type(text)
            elif ev.key == K_c:
                text += "c"
                type(text)
            elif ev.key == K_d:
                text += "d"
                type(text)
            elif ev.key == K_e:
                text += "e"
                type(text)
            elif ev.key == K_f:
                text += "f"
                type(text)
            elif ev.key == K_g:
                text += "g"
                type(text)
            elif ev.key == K_h:
                text += "h"
                type(text)
            elif ev.key == K_i:
                text += "i"
                type(text)
            elif ev.key == K_j:
                text += "j"
                type(text)
            elif ev.key == K_k:
                text += "k"
                type(text)
            elif ev.key == K_l:
                text += "l"
                type(text)
            elif ev.key == K_m:
                text += "m"
                type(text)
            elif ev.key == K_n:
                text += "n"
                type(text)
            elif ev.key == K_o:
                text += "o"
                type(text)
            elif ev.key == K_p:
                text += "p"
                type(text)
            elif ev.key == K_q:
                text += "q"
                type(text)
            elif ev.key == K_r:
                text += "r"
                type(text)
            elif ev.key == K_s:
                text += "s"
                type(text)
            elif ev.key == K_t:
                text += "t"
                type(text)
            elif ev.key == K_u:
                text += "u"
                type(text)
            elif ev.key == K_v:
                text += "v"
                type(text)
            elif ev.key == K_w:
                text += "w"
                type(text)
            elif ev.key == K_x:
                text += "x"
                type(text)
            elif ev.key == K_y:
                text += "y"
                type(text)
            elif ev.key == K_z:
                text += "z"
                type(text)
            elif ev.key == K_SPACE:
                text += " "
                type(text)
            elif ev.key == K_BACKSPACE:
                text = text[0:-1]
                type(text)

    if keyinput[pygame.K_LEFT] and sprite_rect.centerx > 0:
        sprite_rect.centerx -= 10
    elif keyinput[pygame.K_RIGHT] and sprite_rect.centerx < size[0]:
        sprite_rect.centerx += 10


    screen.blit(sprite, sprite_rect)
    pygame.display.flip()