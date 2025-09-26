import sys, atexit
from grid import *

# Fonction utilitaire pour cacher le curseur dans la console
def hideCursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def printScore(score):
    gotoxy(0, HEIGHT + 2)
    print(f"Score : {score}")



