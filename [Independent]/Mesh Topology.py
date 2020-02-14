
import pygame as pg
pg.init()

clockEvent = pg.USEREVENT+1
pg.time.set_timer(clockEvent, 100)

class dot(object):
    dotList = []
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pg.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)

screenX = 1080
screenY = 720

win = pg.display.set_mode((screenX, screenY))
pg.display.set_caption('Mesh Topology')

clock = pg.time.Clock()

lineCount = 0

gridWidth = 3
gridHeight = 3

for x in range(100, (gridWidth+1)*100, 100):
    for y in range(100, (gridHeight+1)*100, 100):
        dot.dotList.append(dot(x, y, 5))

def updateWin():
    for i in dot.dotList:
        i.draw()

while True:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == clockEvent:
            pass

    for i in dot.dotList:
        for j in dot.dotList:
            pg.draw.line(win, (204, 255, 255), (i.x, i.y), (j.x, j.y))

    updateWin()
    pg.display.flip()
