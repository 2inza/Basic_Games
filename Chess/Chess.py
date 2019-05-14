import pygame
from pygame.locals import *
import sys
pg = pygame
pg.init()
# =========================================================
# interface
# =========================================================

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = [800, 566]

fps = pg.time.Clock()
Exit = False
preGame = True
PickWhite = True
PieceSelect = False
temp = 0
x, y = 0, 0
oldX, oldY, = 0, 0

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

while not Exit:
    # fps, Mouse info
    fps.tick(30)
    MousePos = pg.mouse.get_pos()
    MouseClick = pg.mouse.get_pressed()
    # =====================================================================================
    # pregame
    scr.fill(WHITE)
    scr.blit(board, (3, 3))
    scr.blit(me, (700, 545))
    scr.blit(textSurfaceObj, (655, 10))

    act = False
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            Exit = True
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONUP:
            act = True

    if MouseClick[0]:
        if 3 < MousePos[0] < 73: x = 0
        elif MousePos[0] < 143: x = 1
        elif MousePos[0] < 213: x = 2
        elif MousePos[0] < 283: x = 3
        elif MousePos[0] < 353: x = 4
        elif MousePos[0] < 423: x = 5
        elif MousePos[0] < 493: x = 6
        elif MousePos[0] < 563: x = 7
        else: x = "None"

        if 3 < MousePos[1] < 73: y = 0
        elif MousePos[1] < 143: y = 1
        elif MousePos[1] < 213: y = 2
        elif MousePos[1] < 283: y = 3
        elif MousePos[1] < 353: y = 4
        elif MousePos[1] < 423: y = 5
        elif MousePos[1] < 493: y = 6
        elif MousePos[1] < 563: y = 7
        else: y = "None"

    if preGame:
        pg.draw.rect(scr, BLACK, [588, 40, 90, 30], 1)
        pg.draw.rect(scr, BLACK, [688, 40, 90, 30], 1)
        scr.blit(text1Obj, (620, 80))
        scr.blit(button1, (613, 45))
        scr.blit(button2, (714, 45))
        if 588 < MousePos[0] < 678 and 40 < MousePos[1] < 70:
            pg.draw.rect(scr, BLACK, [588, 40, 90, 30], 5)
            if MouseClick[0]:
                preGame = False
        elif 688 < MousePos[0] < 778 and 40 < MousePos[1] < 70:
            pg.draw.rect(scr, BLACK, [688, 40, 90, 30], 5)
            if MouseClick[0]:
                preGame = False
                PickWhite = False

        BoardArray = [[[5, 3, 2, 8, 9, 2, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -2, -8, -9, -2, -3, -5]],

                      [[-5, -3, -2, -9, -8, -2, -3, -5],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [5, 3, 2, 9, 8, 2, 3, 5]]]

        PieceSelect = False
        temp = 0
        oldX, oldY, = 0, 0
        Turn = 1
    # =====================================================================================
    if not preGame:
        pg.draw.rect(scr, BLACK, [588, 532, 90, 30], 1)
        scr.blit(button3, (615, 537))
        if 590 < MousePos[0] < 680 and 532 < MousePos[1] < 562:
            pg.draw.rect(scr, BLACK, [590, 532, 90, 30], 5)
            if MouseClick[0]:
                preGame = True
                PickWhite = True

        if Turn % 2 == 1:
            pg.draw.rect(scr, BLACK, [588, 40, 90, 30], 1)
            scr.blit(button1, (613, 45))
        else:
            pg.draw.rect(scr, BLACK, [688, 40, 90, 30], 1)
            scr.blit(button2, (714, 45))

        for h in range(8):
            for w in range(8):
                if BoardArray[PickWhite][h][w] < 0:
                    if BoardArray[PickWhite][h][w] * -1 == 5:
                        scr.blit(bRook, ((w * 70) + 1, (h * 70) + 2))
                    elif BoardArray[PickWhite][h][w] * -1 == 3:
                        scr.blit(bKnight, ((w * 70) + 1, (h * 70) + 2))
                    elif BoardArray[PickWhite][h][w] * -1 == 2:
                        scr.blit(bBishop, ((w * 70) + 1, (h * 70) + 2))
                    elif BoardArray[PickWhite][h][w] * -1 == 9:
                        scr.blit(bQueen, ((w * 70) + 1, (h * 70) + 2))
                    elif BoardArray[PickWhite][h][w] * -1 == 8:
                        scr.blit(bKing, ((w * 70) + 1, (h * 70) + 2))
                    elif BoardArray[PickWhite][h][w] * -1 == 1:
                        scr.blit(bPawn, ((w * 70) + 1, (h * 70) + 2))
                else:
                    if BoardArray[PickWhite][h][w] == 5:
                        scr.blit(wRook, ((w * 70) + 1, (h * 70) + 3))
                    elif BoardArray[PickWhite][h][w] == 3:
                        scr.blit(wKnight, ((w * 70) + 1, (h * 70) + 3))
                    elif BoardArray[PickWhite][h][w] == 2:
                        scr.blit(wBishop, ((w * 70) + 1, (h * 70) + 3))
                    elif BoardArray[PickWhite][h][w] == 9:
                        scr.blit(wQueen, ((w * 70) + 1, (h * 70) + 3))
                    elif BoardArray[PickWhite][h][w] == 8:
                        scr.blit(wKing, ((w * 70) + 1, (h * 70) + 3))
                    elif BoardArray[PickWhite][h][w] == 1:
                        scr.blit(wPawn, ((w * 70) + 1, (h * 70) + 3))

        if MouseClick[0] and act and x != "None" and y != "None":
            if Turn % 2 == 1:
                if BoardArray[PickWhite][y][x] != 0 and PieceSelect:
                    if (temp > 0) == (BoardArray[PickWhite][y][x] > 0):
                        PieceSelect = False
                        temp = 0
                        print("select cancel")
                    else:
                        BoardArray[PickWhite][y][x] = temp
                        BoardArray[PickWhite][oldY][oldX] = 0
                        oldX, oldY = 0, 0
                        temp = 0
                        PieceSelect = False
                        Turn += 1
                        print("get piece")
                elif 0 < BoardArray[PickWhite][y][x] != 0 and not PieceSelect:
                    temp = BoardArray[PickWhite][y][x]
                    oldX, oldY = x, y
                    PieceSelect = True
                    print("select")
                elif BoardArray[PickWhite][y][x] == 0 and PieceSelect:
                    BoardArray[PickWhite][oldY][oldX] = 0
                    oldX, oldY = 0, 0
                    BoardArray[PickWhite][y][x] = temp
                    temp = 0
                    PieceSelect = False
                    Turn += 1
                    print("move to empty")
            elif Turn % 2 == 0:
                if BoardArray[PickWhite][y][x] != 0 and PieceSelect:
                    if (temp < 0) == (BoardArray[PickWhite][y][x] < 0):
                        PieceSelect = False
                        temp = 0
                        print("select cancel")
                    else:
                        BoardArray[PickWhite][y][x] = temp
                        BoardArray[PickWhite][oldY][oldX] = 0
                        temp = 0
                        PieceSelect = False
                        Turn += 1
                        print("get piece")
                elif 0 > BoardArray[PickWhite][y][x] != 0 and not PieceSelect:
                    temp = BoardArray[PickWhite][y][x]
                    oldX, oldY = x, y
                    PieceSelect = True
                    print("select")
                elif BoardArray[PickWhite][y][x] == 0 and PieceSelect:
                    BoardArray[PickWhite][oldY][oldX] = 0
                    oldX, oldY = 0, 0
                    BoardArray[PickWhite][y][x] = temp
                    temp = 0
                    PieceSelect = False
                    Turn += 1
                    print("move to empty")
    pg.display.flip()



