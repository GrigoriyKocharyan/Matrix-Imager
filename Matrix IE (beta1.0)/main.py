from pygame import *


init()
win = display.set_mode((500,500))
display.set_caption('Matrix ImageEdit')




scene = 0

tfile = None

while 1:

    m = mouse.get_pos()

    win.fill((50, 50, 50))
    for i in event.get():
        if i.type == QUIT:
            quit()
            exit()
        if scene == 2:
            if i.type == DROPBEGIN:
                print(i)
            if i.type == DROPCOMPLETE:
                print(i)
            if i.type == DROPFILE:
                ft = i.file[-3:]
                if ft in ["png", "jpg", "bmp"]:

                    tfile = image.load(i.file)

    if tfile:
        win.blit(tfile, (0,0))


    if scene == 0:
        draw.rect(win, (0, 100, 255), (30, 300, 250, 60), 0, 15)
        if (m[0] >= 30 and m[0] <= 280) and (m[1] >= 300 and m[1] <= 360):
            draw.rect(win, (0, 150, 255), (30, 300, 250, 60), 0, 15)




    display.flip()