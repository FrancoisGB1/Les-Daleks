import os 
import msvcrt

WIDTH = 32
HEIGHT = 16

MOVES = {
    "up":    (0, -1),
    "down":  (0,  1),
    "left":  (-1, 0),
    "right": (1,  0),
}

#Gemini google code
def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')


def drawOutline():
    # top and bottom borders
    for x in range(1, WIDTH + 1):
        gotoxy(x, 1)
        print("-", end="")
        gotoxy(x, HEIGHT)
        print("-", end="")
    # left and right borders
    for y in range(2, HEIGHT):  # skip corners
        gotoxy(1, y)
        print("|", end="")
        gotoxy(WIDTH, y)
        print("|", end="")

def calcMiddle():
    x = WIDTH // 2
    y = HEIGHT // 2
    return x, y