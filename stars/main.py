# STAR GAME
# ===================================
# Module, init
import pygame
from pygame.locals import *
import sys
import random
pg = pygame
pg.init()
# ===================================
# Variable define
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fps = pg.time.Clock()
fps.tick(15)
Shutdown = False
preGame = True
Playing = False
Size = 5
BoardStart = 0
degree = 0
x, y = Size // 2, Size // 2
scr = pg.display.set_mode([600, 800])
# ===================================
# Font, image, strings.
pg.display.set_caption("Star.1")
char = pg.image.load("image/char_in_grid.png")
grid = pg.image.load("image/grid.png")
star = pg.image.load("image/star_in_grid.png")

TitleFont = pg.font.Font('C:\Windows\Fonts\Georgia.ttf', 22)
MainFont = pg.font.Font('C:\Windows\Fonts\Georgia.ttf', 15)

Title = TitleFont.render("Get these Stars!", True, WHITE)
InputBoardSize = MainFont.render("select size of board. at least 5, max 15.", True, WHITE)
Guide = MainFont.render("Press Up key to increase size of board,", True, WHITE)
Guide2 = MainFont.render("Press Down key to decrease size of board.", True, WHITE)
StartKey = MainFont.render("Press Enter to start game, ESC to shutdown game.", True, WHITE)

KeyGuide = MainFont.render("Direction Keys : Move to direction", True, WHITE)
KeyGuide2 = MainFont.render("ESC : Reset", True, WHITE)
# ===================================
# main loop, print Background
while not Shutdown:
    scr.fill(BLACK)
    # ===================================
    # Key setting
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Shutdown = True
            pg.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                if not preGame:
                    y -= 1
                    degree = 90
                elif Size == 15:
                    break
                else:
                    Size += 2
            elif event.key == K_DOWN:
                if not preGame:
                    y += 1
                    degree = 270
                elif Size == 5:
                    break
                else:
                    Size -= 2
            elif event.key == K_LEFT:
                if not preGame:
                    x -= 1
                    degree = 180
            elif event.key == K_RIGHT:
                if not preGame:
                    x += 1
                    degree = 0
            elif event.key == K_RETURN:
                preGame = False
                pg.mixer.music.stop()
            elif event.key == K_ESCAPE:
                if preGame:
                    Shutdown = True
                    pg.quit()
                    sys.exit()
                else:
                    preGame = True
                    pg.mixer.music.stop()
    if y < 0:
        y += 1
    elif y > (Size - 1):
        y -= 1
    elif x < 0:
        x += 1
    elif x > (Size - 1):
        x -= 1
    # ===================================
    # PreGame, reset scores, variables, and print text.
    if preGame:
        if not pg.mixer.music.get_busy():
            pg.mixer.music.load("bgm/main.mp3")
            pg.mixer.music.play(0)
        score = 0
        x, y = Size // 2, Size // 2
        RandomX, RandomY = random.randrange(0, Size - 1), random.randrange(0, Size - 1)
        scr.blit(Title, (225, 320))
        scr.blit(InputBoardSize, (175, 350))

        NumberInput = MainFont.render(str(Size), True, WHITE)
        pg.draw.rect(scr, WHITE, [255, 380, 90, 30], 1)
        scr.blit(NumberInput, (295, 385))

        scr.blit(Guide, (175, 420))
        scr.blit(Guide2, (165, 440))
        scr.blit(StartKey, (130, 460))
    # ===================================
    # in Game, in game algorithms, and print png files and some text.
    else:
        if not pg.mixer.music.get_busy():
            pg.mixer.music.load("bgm/ingame.mp3")
            pg.mixer.music.play(0)
        if Size == 5:
            BoardStart = 200
        elif Size == 7:
            BoardStart = 170
        elif Size == 9:
            BoardStart = 120
        elif Size == 11:
            BoardStart = 80
        elif Size == 13:
            BoardStart = 40
        else:
            BoardStart = 0

        rotated = pg.transform.rotate(char, degree)
        Board = [[0] * Size for x in range(Size)]
        Board[y][x] = 9
        Board[RandomY][RandomX] = 1
        if RandomY == y and RandomX == x:
            Board[y][x] = 9
            RandomX, RandomY = random.randrange(0, Size - 1), random.randrange(0, Size - 1)
            score += 1

        for h in range(Size):
            for w in range(Size):
                if Board[h][w] == 0:
                    scr.blit(grid, ((w * 40 + BoardStart), (h * 40 + BoardStart)))
                elif Board[h][w] == 1:
                    scr.blit(star, ((w * 40 + BoardStart), (h * 40 + BoardStart)))
                elif Board[h][w] == 9:
                    scr.blit(rotated, ((w * 40 + BoardStart), (h * 40 + BoardStart)))
        scr.blit(KeyGuide, (100, 700))
        scr.blit(KeyGuide2, (420, 700))
        Score = MainFont.render(("Your Score : " + str(score)), True, WHITE)
        scr.blit(Score, (260, 650))
    # ===================================
    # refresh frame 15 time per sec.
    pg.display.flip()
