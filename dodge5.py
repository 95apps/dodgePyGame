"""
Brendan Wu
May 6 2017
Submitted to ICS 3U1 - Mr. Cope

dodge.py - an arcade survival game

Version 5 : asteroids get destroyed on correct text
+ text also spawns and falls


"""

import pygame
from pygame.locals import *
import random


pygame.init()

myfont = pygame.font.SysFont("Arial", 30)

size = (400, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TYPE CRISIS")
randomwords = open("randomwords.csv","r")
wordlist = []
activeWordList = []
background = pygame.image.load("background.png")
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
text = ""
time = 0
keep_going = True

for i in randomwords:
    wordlist.append(i.split(",")[0:-1])

asteroids = ["Asteroid1.png","Asteroid2.png","Asteroid3.png","Asteroid4.png","Asteroid6.png","Asteroid7.png","Asteroid8.png"]



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #construct the parent component
        asteroidImage = asteroids[random.randint(0, len(asteroids)-1)] #pick a random asteroid sprite
        self.image = pygame.image.load(asteroidImage) #load randomly picked asteroid
        self.rect = self.image.get_rect() #loads the rect from the image
        #set the position, direction, and speed of the ball
        self.rect.left = random.randrange(0,screen.get_width()-50)
        self.rect.top = -100
        self.dir_x = 0
        self.dir_y = 1
        self.speed = random.randrange(1,2)
        self.word = random.choice(wordlist)


    def update(self):
        #Handle the walls by changing direction(s)

        if self.rect.left < 0 or self.rect.right >= screen.get_width():
            self.dir_x *= -1
        if self.rect.bottom >= screen.get_height():
            keep_going = False

        self.rect.move_ip(self.speed*self.dir_x, self.speed*self.dir_y)


        if(self.word[0] == text):
            print("KILLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
            self.kill()


        else:
            print(self.word[0])

class Word(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #construct the parent component
        asteroidImage = asteroids[random.randint(0, len(asteroids)-1)] #pick a random asteroid sprite
        self.word = random.choice(wordlist)
        self.image = myfont.render(str(self.word), False, (0, 0, 0))
        self.rect = self.image.get_rect() #loads the rect from the image
        #set the position, direction, and speed of the ball
        self.rect.left = random.randrange(0,screen.get_width()-50)
        self.rect.top = -100
        self.dir_x = 0
        self.dir_y = 1
        self.speed = random.randrange(1,2)



    def update(self):
        #Handle the walls by changing direction(s)

        if self.rect.left < 0 or self.rect.right >= screen.get_width():
            self.dir_x *= -1
        if self.rect.bottom >= screen.get_height():
            keep_going = False

        self.rect.move_ip(self.speed*self.dir_x, self.speed*self.dir_y)


        if(self.word[0] == text):
            print("KILLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
            self.kill()


        else:
            print(self.word[0])




def type(text):
   chars = len(text)
   screen.blit(background, (0,0))
   font=pygame.font.SysFont("Arial",28)
   typetext=font.render(text.upper(), 1,(255,255,255))
   screen.blit(typetext, (size[0] //2 - 6.5 * chars, size[1] - 150))
   label = myfont.render(str(seconds), 1, (255, 255, 255))
   screen.blit(label, (4, 0))



ball_group = pygame.sprite.Group()
word_group = pygame.sprite.Group()



seconds = 0
while keep_going:
    print(activeWordList)
    clock.tick(60)
    keyinput = pygame.key.get_pressed()
    time +=1
    if (time% 60 == 0):
        seconds += 1


    if (time % 240 == 0):

         ball = Ball()
         ball_group.add(ball)
         word = Word()
         word_group.add(word)








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
            elif ev.key == K_QUOTE:
                text +="'"
                type(text)
            elif ev.key == K_SPACE:
                text += " "
                type(text)
            elif ev.key == K_BACKSPACE:
                text = ""
                type(text)

    ball_group.clear(screen, background)

    ball_group.update()

    ball_group.draw(screen)

    word_group.clear(screen, background)

    word_group.update()

    word_group.draw(screen)


    pygame.display.flip()
