from pygame import *

init()
win = display.set_mode((500,500))

click = 0
blocks = []

camX = 0
camY = 0



class Block:
    def __init__(self,x,y,cx,cy):
        self.x = x
        self.y = y
        self.cx = cx
        self.cy = cy
    def draw(self):
        draw.rect(win, (0,0,0), (self.cx, self.cy, 50, 50), 5)


while 1:

    m = mouse.get_pos()

    if key.get_pressed()[K_UP]:
        camY -= 50
        time.delay(100)
    if key.get_pressed()[K_DOWN]:
        camY += 50
        time.delay(100)
    if key.get_pressed()[K_RIGHT]:
        camX += 50
        time.delay(100)
    if key.get_pressed()[K_LEFT]:
        camX -= 50
        time.delay(100)


    win.fill((255,255,255))

    for i in event.get():
        if i.type == QUIT:
            quit()
            exit()
        if i.type == MOUSEBUTTONDOWN:
            click = 1
        if i.type == MOUSEBUTTONUP:
            click = 0

    if click:
        click = 0
        blocks.append(Block(round(m[0]/50-camX)*50-25+camY, round(m[1]/50-camY)*50-25+camY, round(m[0]/50)*50-25, round(m[1]/50)*50-25))

    for block in blocks:

        block.cx = block.x-camX
        block.cy = block.y-camY

        block.draw()

    display.flip()
