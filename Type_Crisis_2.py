'''
Claudio Lamonaca and Brendan Wu
May 6, 2017
Submitted to ICS 3U1 - Mr. Cope

dodge7.py - An arcade survival game

working game and menu functionality - not refined and has some graphical issues
- score updating standalone inside type() no longer has to be called on keypress.

+Space_Age.ttf
+space.png
+Logo.png
+A Walk Into Space - Non Copyright Music[Ambient].ogg

'''
import pygame
from pygame.locals import *
import random

pygame.init()

# Game Variables
size = (400, 650)
Temp = 4
time = 0
Temp2 = 1
seconds = 0

# Create Background
background = pygame.image.load("space.png")
screen = pygame.display.set_mode(background.get_size())
background = background.convert()
pygame.display.set_caption("TYPE CRISIS")

# Insert Type Crisis Logo
logo = pygame.image.load('Logo.png')

# Ingame Music
file = ("A Walk Into Space - Non Copyright Music [Ambient].ogg")
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(loops=99)
pygame.mixer.music.set_volume(0.1)

# Game words
myfont = pygame.font.SysFont("Arial", 15)
label = myfont.render("Some text!", 1, (123, 131, 0))

# Menu Font + Labels
largefont = pygame.font.Font("Space_Age.ttf", 50)
label_start = largefont.render("START", 1, (255, 255, 255))
label_help = largefont.render("HELP", 2, (255, 255, 255))
label_credits = largefont.render("CREDITS", 3, (255, 255, 255))
label_GAME = largefont.render("GAME", 3, (255, 255, 255))
label_OVER = largefont.render("OVER", 3, (255, 255, 255))

smallfont = pygame.font.Font("Space_Age.ttf", 25)
label_back = smallfont.render("BACK", 3, (255, 255, 255))

# Paragraph inside Help Screen
middlefont = pygame.font.Font("Space_Age.ttf", 15)
paragraph_help1 = middlefont.render('Type Crisis is a race against time', 1, (255, 255, 255))
paragraph_help2 = middlefont.render('survival game. Protect your ship', 1, (255, 255, 255))
paragraph_help3 = middlefont.render('from asteroids by blowing them', 1, (255, 255, 255))
paragraph_help4 = middlefont.render('up with keystrokes. Type out the', 1, (255, 255, 255))
paragraph_help5 = middlefont.render('correct word to blast the asteroids', 1, (255, 255, 255))
paragraph_help6 = middlefont.render('and survive to fight another day.', 1, (255, 255, 255))
paragraph_help7 = middlefont.render('\n', 1, (255, 255, 255))
paragraph_help8 = middlefont.render('Levels progressively get faster', 1, (255, 255, 255))
paragraph_help9 = middlefont.render('and so will your typing skills.', 1, (255, 255, 255))
paragraph_help11 = middlefont.render('The perfect way to blow time,', 1, (255, 255, 255))
paragraph_help12 = middlefont.render('blow asteroids', 1, (255, 255, 255))
paragraph_help13 = middlefont.render('and blow up your typing skills', 1, (255, 255, 255))

# Credits in the Credit Screen
credits_line1 = middlefont.render('Programming by Claudio and Brendan', 1, (255, 255, 255))
credits_line2 = middlefont.render('+ some StackOverflow', 1, (255, 255, 255))
credits_line3 = middlefont.render('Music by: ', 1, (255, 255, 255))  # Enter music

# Open csv file and insert to list
randomwords = open("THE_ENTIRE_BEE_MOVIE_SCRIPT.csv", "r")
wordlist = []
activeWordList = []
for i in randomwords:
    wordlist.append(i.split(",")[0:-1])

# Asteroids
asteroids = ["asteroid1.png", "asteroid2.png", "asteroid3.png"]


class Ball(pygame.sprite.Sprite):
    def __init__(self, randomWord, position):

        pygame.sprite.Sprite.__init__(self)  # construct the parent component
        asteroidImage = asteroids[random.randint(0, len(asteroids) - 1)]  # pick a random asteroid sprite
        self.image = pygame.image.load(asteroidImage)  # load randomly picked asteroid
        self.rect = self.image.get_rect()  # loads the rect from the image
        # set the position, direction, and speed of the ball
        self.rect.left = position
        self.rect.top = -100
        self.dir_x = 0
        self.dir_y = 1
        self.speed = random.randrange(1, 2)
        self.word = randomWord.upper()

    def update(self):
        # Handle the walls by changing direction(s)

        if self.rect.left < 0 or self.rect.right >= screen.get_width():
            self.dir_x *= -1
        if self.rect.bottom >= screen.get_height():
            global Temp
            Temp = 5

        self.rect.move_ip(self.speed * self.dir_x, self.speed * self.dir_y)

        if (self.word.lower() == text):
            print("KILLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
            self.kill()


        else:
            print(self.word[0])


# Falling Words
class Word(pygame.sprite.Sprite):
    def __init__(self, randomWord, position):

        pygame.sprite.Sprite.__init__(self)  # construct the parent component
        asteroidImage = asteroids[random.randint(0, len(asteroids) - 1)]  # pick a random asteroid sprite
        self.word = randomWord.upper()
        self.image = myfont.render(str(self.word), False, (255, 255, 255))
        self.rect = self.image.get_rect()  # loads the rect from the image
        # set the position, direction, and speed of the ball
        self.rect.left = position
        self.rect.top = -10
        self.dir_x = 0
        self.dir_y = 1
        self.speed = random.randrange(1, 2)

    def update(self):
        # Handle the walls by changing direction(s)

        if self.rect.left < 0 or self.rect.right >= screen.get_width():
            self.dir_x *= -1
        if self.rect.bottom >= screen.get_height():
            global Temp
            Temp = 5

        self.rect.move_ip(self.speed * self.dir_x, self.speed * self.dir_y)

        if (self.word.lower() == text):
            print("KILLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
            self.kill()


        else:
            print(self.word[0])


# Ingame Text
text = ""


def type(text):
    chars = len(text)

    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("Arial", 20)
    typetext = font.render(text.upper(), 1, (255, 255, 255))
    screen.blit(typetext, (size[0] // 2 - 6.5 * chars, size[1] - 150))
    label = myfont.render(str(seconds), 1, (255, 255, 255))

    screen.blit(label, (370, 10))



ball_group = pygame.sprite.Group()
word_group = pygame.sprite.Group()

clock = pygame.time.Clock()

keep_going = True

while keep_going:
    clock.tick(60)

    type(text)


    if (Temp == 1):  # Game

        if Temp2 == 1:
            screen.blit(background, (0, 0))
            Temp2 = 0

        print(activeWordList)
        keyinput = pygame.key.get_pressed()
        time += 1
        if (time % 60 == 0):
            seconds += 1

        if (time % 60 == 0) and (Temp != 5):
            randomWord = random.choice(wordlist)[0]
            position = random.randrange(0,screen.get_width()-150)
            ball = Ball(randomWord,position)
            ball_group.add(ball)
            word = Word(randomWord,position + 25)
            word_group.add(word)

        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
                pygame.quit()
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
                elif ev.key == K_0:
                    text += "0"
                    type(text)
                elif ev.key == K_1:
                    text += "1"
                    type(text)
                elif ev.key == K_2:
                    text += "2"
                    type(text)
                elif ev.key == K_3:
                    text += "3"
                    type(text)
                elif ev.key == K_4:
                    text += "4"
                    type(text)
                elif ev.key == K_5:
                    text += "5"
                    type(text)
                elif ev.key == K_6:
                    text += "6"
                    type(text)
                elif ev.key == K_7:
                    text += "7"
                    type(text)
                elif ev.key == K_8:
                    text += "8"
                    type(text)
                elif ev.key == K_9:
                    text += "9"
                    type(text)
                elif ev.key == K_MINUS:
                    text += "-"
                    type(text)
                elif ev.key == K_SEMICOLON:
                    text += ";"
                    type(text)
                elif ev.key == K_PERIOD:
                    text+="."
                    type(text)
                elif ev.key == K_QUOTE:
                    text += "'"
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

    elif (Temp == 2):  # Help Screen

        for ev in pygame.event.get():

            if ev.type == QUIT:
                keep_going = False
                pygame.quit()
            elif ev.type == MOUSEBUTTONDOWN:  # A mouse click!
                x = ev.pos[0]  # the MOUSEBUTTONDOWN event has a position property
                y = ev.pos[1]  # that is an (x, y) tuple
                print(x, y)

                if (282 <= x <= 368) and (611 <= y <= 622):  # back button
                    Temp = 4

        screen.blit(background, (0, 0))
        screen.blit(label_help, (110, 78.5))
        screen.blit(paragraph_help1, (0, 215))
        screen.blit(paragraph_help2, (0, 230))
        screen.blit(paragraph_help3, (0, 245))
        screen.blit(paragraph_help4, (0, 260))
        screen.blit(paragraph_help5, (0, 275))
        screen.blit(paragraph_help6, (0, 290))
        screen.blit(paragraph_help7, (0, 305))
        screen.blit(paragraph_help8, (0, 320))
        screen.blit(paragraph_help9, (0, 335))
        screen.blit(paragraph_help11, (0, 365))
        screen.blit(paragraph_help12, (0, 380))
        screen.blit(paragraph_help13, (0, 395))
        screen.blit(label_back, (282, 605))
        pygame.display.flip()

    elif (Temp == 3):
        for ev in pygame.event.get():

            if ev.type == QUIT:
                keep_going = False
                pygame.quit()
            elif ev.type == MOUSEBUTTONDOWN:  # A mouse click!
                x = ev.pos[0]  # the MOUSEBUTTONDOWN event has a position property
                y = ev.pos[1]  # that is an (x, y) tuple
                print(x, y)

                if (282 <= x <= 368) and (611 <= y <= 622):  # back button
                    Temp = 4

        screen.blit(background, (0, 0))

        screen.blit(credits_line1, (0, 215))
        screen.blit(credits_line2, (0, 230))
        screen.blit(credits_line3, (0, 245))

        screen.blit(label_credits, (63, 78.5))
        screen.blit(label_back, (282, 605))
        pygame.display.flip()

    elif (Temp == 4):  # Menu


        for ev in pygame.event.get():

            if ev.type == QUIT:
                keep_going = False
                pygame.quit()
            elif ev.type == MOUSEBUTTONDOWN:  # A mouse click!
                x = ev.pos[0]  # the MOUSEBUTTONDOWN event has a position property
                y = ev.pos[1]  # that is an (x, y) tuple
                print(x, y)

                if (96 <= x <= 304) and (402 <= y <= 424):  # Play button
                    Temp = 1


                elif (113 <= x <= 288) and (462 <= y <= 484):  # Help button
                    Temp = 2


                elif (64 <= x <= 340) and (522 <= y <= 544):  # Credits button
                    Temp = 3

        screen.blit(background, (0, 0))
        screen.blit(logo, (0, 0))
        screen.blit(label_start, (94, 388))
        screen.blit(label_help, (112, 448))
        screen.blit(label_credits, (63, 508))
        pygame.display.flip()

    elif Temp == 5:
        Temp2 = 1
        for ev in pygame.event.get():

            if ev.type == QUIT:
                keep_going = False
                pygame.quit()

            elif ev.type == MOUSEBUTTONDOWN:  # A mouse click!
                x = ev.pos[0]  # the MOUSEBUTTONDOWN event has a position property
                y = ev.pos[1]  # that is an (x, y) tuple
                print(x, y)

                if (282 <= x <= 368) and (611 <= y <= 622):  # back button
                    Temp = 4

        for i in ball_group:
            i.kill()

        for k in word_group:
            k.kill()

        screen.blit(background, (0, 0))
        screen.blit(label_GAME, (110, 53.5))
        screen.blit(label_OVER, (110, 128.5))
        screen.blit(label_back, (282, 605))
        pygame.display.flip()









