import os
from grid import *
from Input import *
from util import *


# Main
os.system('cls')
drawOutline()
doctorPos = spawnDoc()

while(1):
    hideCursor()
    oldPos = doctorPos
    newPos = playerInput(doctorPos)
    clearPosition(oldPos)
    printDoc(newPos)
    doctorPos = newPos