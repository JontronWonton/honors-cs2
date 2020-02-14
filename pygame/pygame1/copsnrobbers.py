# Jonathan Klein
# 2/22/19
# copsnrobbers.py

from random import *
import time
import pygame
pygame.init()

pygame.font.init()

font1 = pygame.font.Font(None, 36)
# font2 = pygame.font.Font(None, 100)

score = 0

screenX = 1000
screenY = 720

copWidth = 210
copHeight = 210
copX = screenX/2
copY = screenY/2

pygame.mixer.music.load('bensound-memories.mp3')
pygame.mixer.music.play(-1)

oof = pygame.mixer.Sound('deathsound.wav')

win = pygame.display.set_mode((screenX, screenY))
ghostWin = pygame.Surface((screenX, screenY))
pygame.display.set_caption('Cops and Robbers')
bg = pygame.image.load('tilted.png')
cop = pygame.image.load('robloxcop.png')
robber = pygame.image.load('robloxrobber.png')

robberWidth = 210
robberHeight = 210
robberX = randint(0, screenX-robberWidth)
robberY = randint(0, screenY-robberHeight)

copVelocity = 10

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False

    win.blit(bg, (0, 0))

    scoreText = font1.render(f'Score: {score}', True, (0, 0, 0))
    win.blit(scoreText, (20, 20))

    win.blit(cop, (copX, copY))
    copRectX = copX+(copWidth-110)/2
    copRect = pygame.draw.rect(ghostWin, (255, 255, 255), (copRectX, copY, 110, 210))

    win.blit(robber, (robberX, robberY))
    robberRectWidth = 130
    robberRectHeight = 210
    robberRectX = robberX+(robberWidth-robberRectWidth)/2
    robberRect = pygame.draw.rect(ghostWin, (255, 255, 255), (robberRectX, robberY, robberRectWidth, robberRectHeight))

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and copX > 0:
        copX -= copVelocity
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]  and copX < screenX-copWidth:
        copX += copVelocity
    if keys[pygame.K_UP] or keys[pygame.K_w] and copY > 0:
        copY -= copVelocity
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and copY < screenY-copHeight:
        copY += copVelocity

    if copRect.colliderect(robberRect):
        score += 1
        print(f'HIT! ({score} total)')
        oof.play()
        robberX = randint(0, screenX-robberWidth)
        robberY = randint(0, screenY-robberHeight)

    if score == 10:
        # winText = font2.render('YOU WIN!!!', True, (0, 0, 0))
        # win.blit(winText, ()
        winText = pygame.image.load('victoryroyale.png')
        win.blit(winText, (screenX/2-550, 0))
        pygame.display.update()
        time.sleep(2)
        run = False

pygame.quit()
