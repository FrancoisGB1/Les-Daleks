import os
from grid import *
from Input import *
from util import *
from dalek import *


# Main
os.system('cls')
drawOutline()
doctorPos = spawnDoc()
daleks = [initializeDalek(doctorPos)]
daleks.append(initializeDalek(doctorPos))
printAllDalek(daleks)

while(1):
    hideCursor()
    oldPos = doctorPos
    newPos = playerInput(doctorPos)
    for i in range(len(daleks)):
        clearPosition(daleks[i])
        daleks[i] = moveDalek(daleks[i], doctorPos)
    clearPosition(oldPos)
    printAllDalek(daleks)
    printDoc(newPos)
    doctorPos = newPos