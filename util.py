import sys, atexit
from grid import *

# Fonction utilitaire pour cacher le curseur dans la console
def hideCursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()



