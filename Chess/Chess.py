import pygame
from pygame.locals import *
import sys
pg = pygame
pg.init()
# =========================================================

# interface

# =========================================================
# interface
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = [700, 500]

board = pg.image.load("sources/board.jpg")

wKing = pg.image.load("sources/wking.png")
wQueen = pg.image.load("sources/wqueen.png")
wKnight = pg.image.load("sources/wknight.png")
wBishop = pg.image.load("sources/wbishop.png")
wRook = pg.image.load("sources/wrook.png")
wPawn = pg.image.load("sources/wpawn.png")

bKing = pg.image.load("sources/bking.png")
bQueen = pg.image.load("sources/bqueen.png")
bKnight = pg.image.load("sources/bknight.png")
bBishop = pg.image.load("sources/bbishop.png")
bRook = pg.image.load("sources/brook.png")
bPawn = pg.image.load("sources/bpawn.png")

scr = pg.display.set_mode(SIZE)
pg.display.set_caption("CHESS")

Title = pg.font.Font('C:\Windows\Fonts\Georgia.ttf', 20)
textSurfaceObj = Title.render("Chess", True, BLACK)
text1 = pg.font.Font('C:\Windows\Fonts\Georgia.ttf', 15)
text1Obj = text1.render("Choose your color.", True, BLACK)
me = text1.render("made by Yeon", True, BLACK)
button1 = text1.render("White", True, BLACK)
button2 = text1.render("Black", True, BLACK)
button3 = text1.render("Reset", True, BLACK)
# =========================================================

fps = pg.time.Clock()
Exit = False
preGame = False
PickWhite = True
Moving = (0, 0)
while not Exit:
    # fps
    fps.tick(15)

    # ===============================================
    # first screen.
    scr.fill(WHITE)
    scr.blit(board, (0, 0))
    scr.blit(me, (600, 480))
    scr.blit(textSurfaceObj, (565, 10))
    # ===============================================

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            Exit = True
            pg.quit()
            sys.exit()

    MousePos = pg.mouse.get_pos()
    MouseClick = pg.mouse.get_pressed()
    if not preGame:
        pg.draw.rect(scr, BLACK, [500, 40, 90, 30], 1)
        pg.draw.rect(scr, BLACK, [600, 40, 90, 30], 1)
        scr.blit(text1Obj, (535, 80))
        scr.blit(button1, (525, 45))
        scr.blit(button2, (625, 45))
        if 500 < MousePos[0] < 590 and 40 < MousePos[1] < 70:
            pg.draw.rect(scr, BLACK, [500, 40, 90, 30], 5)
            if MouseClick[0]:
                preGame = True
        elif 600 < MousePos[0] < 690 and 40 < MousePos[1] < 70:
            pg.draw.rect(scr, BLACK, [600, 40, 90, 30], 5)
            if MouseClick[0]:
                preGame = True
                PickWhite = False

    if preGame:
        pg.draw.rect(scr, BLACK, [500, 465, 90, 30], 1)
        scr.blit(button3, (527, 470))
        if 500 < MousePos[0] < 590 and 465 < MousePos[1] < 495:
            pg.draw.rect(scr, BLACK, [500, 465, 90, 30], 5)
            if MouseClick[0]:
                preGame = False
                PickWhite = True
        if PickWhite:
            scr.blit(bRook, (13 + Moving[0], 11 + Moving[1]))
            scr.blit(bKnight, (73 + Moving[0], 11 + Moving[1]))
            scr.blit(bBishop, (136 + Moving[0], 11 + Moving[1]))
            scr.blit(bQueen, (195 + Moving[0], 11 + Moving[1]))
            scr.blit(bKing, (255 + Moving[0], 11 + Moving[1]))
            scr.blit(bBishop, (315 + Moving[0], 11 + Moving[1]))
            scr.blit(bKnight, (375 + Moving[0], 11 + Moving[1]))
            scr.blit(bRook, (435 + Moving[0], 11 + Moving[1]))

            scr.blit(wRook, (13 + Moving[0], 433 + Moving[1]))
            scr.blit(wKnight, (73 + Moving[0],433 + Moving[1]))
            scr.blit(wBishop, (136 + Moving[0], 433 + Moving[1]))
            scr.blit(wQueen, (195 + Moving[0], 433 + Moving[1]))
            scr.blit(wKing, (255 + Moving[0], 433 + Moving[1]))
            scr.blit(wBishop, (315 + Moving[0], 433 + Moving[1]))
            scr.blit(wKnight, (375 + Moving[0], 433 + Moving[1]))
            scr.blit(wRook, (435 + Moving[0], 433 + Moving[1]))

            scr.blit(bPawn, (11 + Moving[0], 71 + Moving[1]))
            scr.blit(bPawn, (72 + Moving[0], 71 + Moving[1]))
            scr.blit(bPawn, (133 + Moving[0], 71 + Moving[1]))
            scr.blit(bPawn, (194 + Moving[0], 71 + Moving[1]))
            scr.blit(bPawn, (255 + Moving[0], 71 + Moving[1]))
            scr.blit(bPawn, (316 + Moving[0], 71 + Moving[1]))
            scr.blit(bPawn, (377 + Moving[0], 71 + Moving[1]))
            scr.blit(bPawn, (438 + Moving[0], 71 + Moving[1]))

            scr.blit(wPawn, (11 + Moving[0], 373 + Moving[1]))
            scr.blit(wPawn, (72 + Moving[0], 373 + Moving[1]))
            scr.blit(wPawn, (133 + Moving[0], 373 + Moving[1]))
            scr.blit(wPawn, (194 + Moving[0], 373 + Moving[1]))
            scr.blit(wPawn, (255 + Moving[0], 373 + Moving[1]))
            scr.blit(wPawn, (316 + Moving[0], 373 + Moving[1]))
            scr.blit(wPawn, (377 + Moving[0], 373 + Moving[1]))
            scr.blit(wPawn, (438 + Moving[0], 373 + Moving[1]))

        if not PickWhite:
            scr.blit(wRook, (13 + Moving[0], 11 + Moving[1]))
            scr.blit(wKnight, (73 + Moving[0], 11 + Moving[1]))
            scr.blit(wBishop, (136 + Moving[0], 11 + Moving[1]))
            scr.blit(wKing, (195 + Moving[0], 11 + Moving[1]))
            scr.blit(wQueen, (255 + Moving[0], 11 + Moving[1]))
            scr.blit(wBishop, (315 + Moving[0], 11 + Moving[1]))
            scr.blit(wKnight, (375 + Moving[0], 11 + Moving[1]))
            scr.blit(wRook, (435 + Moving[0], 11 + Moving[1]))

            scr.blit(bRook, (13 + Moving[0], 433 + Moving[1]))
            scr.blit(bKnight, (73 + Moving[0], 433 + Moving[1]))
            scr.blit(bBishop, (136 + Moving[0], 433 + Moving[1]))
            scr.blit(bKing, (195 + Moving[0], 433 + Moving[1]))
            scr.blit(bQueen, (255 + Moving[0], 433 + Moving[1]))
            scr.blit(bBishop, (315 + Moving[0], 433 + Moving[1]))
            scr.blit(bKnight, (375 + Moving[0], 433 + Moving[1]))
            scr.blit(bRook, (435 + Moving[0], 433 + Moving[1]))

            scr.blit(wPawn, (11 + Moving[0], 71 + Moving[1]))
            scr.blit(wPawn, (72 + Moving[0], 71 + Moving[1]))
            scr.blit(wPawn, (133 + Moving[0], 71 + Moving[1]))
            scr.blit(wPawn, (194 + Moving[0], 71 + Moving[1]))
            scr.blit(wPawn, (255 + Moving[0], 71 + Moving[1]))
            scr.blit(wPawn, (316 + Moving[0], 71 + Moving[1]))
            scr.blit(wPawn, (377 + Moving[0], 71 + Moving[1]))
            scr.blit(wPawn, (438 + Moving[0], 71 + Moving[1]))

            scr.blit(bPawn, (11 + Moving[0], 373 + Moving[1]))
            scr.blit(bPawn, (72 + Moving[0], 373 + Moving[1]))
            scr.blit(bPawn, (133 + Moving[0], 373 + Moving[1]))
            scr.blit(bPawn, (194 + Moving[0], 373 + Moving[1]))
            scr.blit(bPawn, (255 + Moving[0], 373 + Moving[1]))
            scr.blit(bPawn, (316 + Moving[0], 373 + Moving[1]))
            scr.blit(bPawn, (377 + Moving[0], 373 + Moving[1]))
            scr.blit(bPawn, (438 + Moving[0], 373 + Moving[1]))
    pg.display.flip()



