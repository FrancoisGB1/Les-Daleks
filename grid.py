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
    """Déplace le curseur de la console à une position donnée.

    :param x: Coordonnée horizontale (colonne).
    :type x: int

    :param y: Coordonnée verticale (ligne).
    :type y: int
    """
    print(f"\033[{y};{x}H", end='')


def drawOutline():
    """Dessine les bordures de la grille de jeu et affiche les instructions de base.
    
    La fonction trace les lignes horizontales et verticales,
    puis affiche les indications pour quitter le jeu et le score initial.
    """
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
        
    gotoxy(0, HEIGHT + 1)
    print("Press 'Q' to quit")
    gotoxy(0, HEIGHT + 2)
    print("Score : 0")
    gotoxy(0, HEIGHT + 3)
    print(f"Zapper(Z) cooldown : 4/4")
    gotoxy(0, HEIGHT + 4)
    print(f"Teleporter(T) cooldown : 4/4")


def calcMiddle():
    """Calcule la position centrale de la grille.

    :return: Coordonnées du centre de la grille.
    :rtype: tuple (int, int)
    """
    x = WIDTH // 2
    y = HEIGHT // 2
    return x, y
