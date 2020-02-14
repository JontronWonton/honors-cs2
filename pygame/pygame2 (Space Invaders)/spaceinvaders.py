# Jonathan Klein
# 3/14/19
# spaceinvaders.py

import pygame as pg
import time, sys
pg.init()

class Ship(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 15
        self.delay = 0
        self.image = pg.transform.scale(pg.image.load('spaceship.png'), (90, 130))
        self.rect = pg.Rect(x, y, width, height)

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > 0:
            self.x -= self.velocity
        if keys[pg.K_RIGHT] and self.x < screenWidth - self.velocity - self.width:
            self.x += self.velocity


class Projectile(pg.sprite.Sprite):
    projectiles = []
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 20
        self.image = pg.transform.scale(pg.image.load('spriteCranberry.png'), (width, height))
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def collide(self, obj):
        if pg.sprite.collide_rect(self, obj):
            print('HIT')


class Entity(pg.sprite.Sprite):
    entities = []
    def __init__(self, x, y, width, height, image):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.delay = 0
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = pg.Rect(x, y, width, height)
        self.dir = 1

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)


def updateWin():
    win.blit(bg, (0, 0))
    user.draw()
    win.blit(scoreText, (10, 10))
    win.blit(timeText, (screenWidth-240, 10))
    for p in Projectile.projectiles:
        p.draw(win)
    for e in Entity.entities:
        e.draw()
    pg.display.update()

screenWidth = 1080
screenHeight = 720
win = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption('Space Invaders')

clockEvent = pg.USEREVENT+1
pg.time.set_timer(clockEvent, 200)

font = pg.font.Font(None, 36)
youWin = pg.image.load('youWin.png')

pg.mixer.music.load('Divinity.mp3')

hitSound = pg.mixer.Sound('boop.wav')
hitSound.set_volume(0.5)
welcomeSound = pg.mixer.Sound('welcome.wav')
welcomeSound.set_volume(0.75)
winSound = pg.mixer.Sound('yay.wav')
winSound.set_volume(0.25)

winDelay = 0
tick = 0
score = 0
noneWasted = True
winBool = False

bg = pg.transform.scale(pg.image.load('welcome.jpg'), (1080, 720))

welcome = True

while welcome:
    pg.time.delay(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            welcomeSound.play()
            time.sleep(1)
            welcome = False

    win.blit(bg, (screenWidth/2-bg.get_width()/2, screenHeight/2-bg.get_height()/2))
    pg.display.update()

pg.mixer.music.play(-1)

bg = pg.image.load('8bitspace.png')
user = Ship(screenWidth/2-45, screenHeight-140, 90, 130)

for i in range(0, screenWidth, 110):
    Entity.entities.append(Entity(i, 10, 80, 80, 'alien.png'))

level1 = True
while level1:
    pg.time.delay(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == clockEvent:
            if winBool:
                winDelay += 1
            else:
                tick += 0.2

            if user.delay <= 0:
                user.delay += 1

            for e in Entity.entities:
                e.delay += 5
                if (e.delay + 20) % 20 == 10:
                    e.y += 10
                elif e.delay % 20 == 0:
                    e.dir *= -1
                    e.x += 10*e.dir

    for p in Projectile.projectiles:
        for e in Entity.entities:
            if p.y - p.width < e.rect[1] + e.rect[3] and p.y + p.width > e.rect[1]:
                if p.x + p.width > e.rect[0] and p.x - p.width < e.rect[0] + e.rect[2]:
                    print(f'({tick}) Entity at ({e.x}, {e.y}) hit')
                    score += 1
                    hitSound.play()
                    Entity.entities.pop(Entity.entities.index(e))
                    Projectile.projectiles.pop(Projectile.projectiles.index(p))
        if p.y > 0:
            p.y -= p.velocity
        else:
            Projectile.projectiles.pop(Projectile.projectiles.index(p))
            noneWasted = False

    scoreText = font.render(f'Score: {score}', True, (255, 255, 255))
    timeText = font.render(f'Time: {round(tick, 2)} seconds', True, (255, 255, 255))

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE] or keys[pg.K_UP]:
        if user.delay > 0 and not winBool:
            Projectile.projectiles.append(Projectile(user.x+29, user.y-40, 32, 32))
            user.delay -= 1

    user.move()

    if len(Entity.entities) == 0: # If user wins
        winBool = True
        winSound.play()
        if winDelay >= 10:
            print(f'({tick}) Level One Complete')
            win.blit(youWin, (screenWidth/2-youWin.get_width()/2, screenHeight/2-youWin.get_height()/2))
            pg.display.update()
            time.sleep(1)
            level1 = False
    updateWin()

Projectile.projectiles = []

level2 = True
winDelay = 0
winBool = False

bg = pg.image.load('8bitspace2.jpg')
score = 0

for i in range(0, screenWidth, 110):
    Entity.entities.append(Entity(i, 10, 75, 75, 'alien2.png'))

for i in range(0, screenWidth, 110):
    Entity.entities.append(Entity(i, 110, 75, 75, 'alien2.png'))

while level2:
    pg.time.delay(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == clockEvent:
            if winBool:
                winDelay += 1
            else:
                tick += 0.2

            if user.delay <= 0:
                user.delay += 1

            for e in Entity.entities:
                e.delay += 5
                if (e.delay + 20) % 20 == 10:
                    e.y += 10
                elif e.delay % 20 == 0:
                    e.dir *= -1
                    e.x += 10*e.dir

    keys = pg.key.get_pressed()

    for p in Projectile.projectiles:
        for e in Entity.entities:
            if p.y - p.width < e.rect[1] + e.rect[3] and p.y + p.width > e.rect[1]:
                if p.x + p.width > e.rect[0] and p.x - p.width < e.rect[0] + e.rect[2]:
                    print(f'({tick}) Entity at ({e.x}, {e.y}) hit')
                    score += 1
                    winSound.stop()
                    hitSound.play()
                    Entity.entities.pop(Entity.entities.index(e))
                    Projectile.projectiles.pop(Projectile.projectiles.index(p))
        if p.y > 0:
            p.y -= p.velocity
        else:
            Projectile.projectiles.pop(Projectile.projectiles.index(p))
            noneWasted = False

    scoreText = font.render(f'Score: {score}', True, (255, 255, 255))
    timeText = font.render(f'Time: {round(tick, 2)} seconds', True, (255, 255, 255))

    if keys[pg.K_SPACE] or keys[pg.K_UP]: # If user shoots a projectile
        if user.delay > 0 and not winBool:
            Projectile.projectiles.append(Projectile(user.x+29, user.y-40, 32, 32))
            user.delay -= 1

    user.move()

    if len(Entity.entities) == 0: # If user wins
        winBool = True
        winSound.play()
        if winDelay >= 10:
            print(f'({tick}) Level Two Complete')
            win.blit(youWin, (screenWidth/2-youWin.get_width()/2, screenHeight/2-youWin.get_height()/2))
            pg.display.update()
            time.sleep(1)
            level2 = False

    updateWin()

print('Thanks for playing :)')
pg.quit()
