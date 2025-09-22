import os
from grid import *
from Input import *
from util import *
from dalek import *


# Main
os.system('cls')
drawOutline()
doctorPos = spawnDoc()
daleks = []
daleks.append(initializeDalek(doctorPos))
printAllDalek(daleks)

while(1):
    hideCursor()
    oldPos = doctorPos
    newPos = playerInput(doctorPos)
    clearPosition(oldPos)
    printDoc(newPos)
    doctorPos = newPos