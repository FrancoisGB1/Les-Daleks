import os
from grid import *
from Input import *
from util import *
from dalek import *


# Main

replay = True

while replay:
    isAlive = True
    replay = True
    replayInput = ''
    os.system('cls')
    drawOutline()
    doctorPos = spawnDoc()
    daleks = [initializeDalek(doctorPos)]
    daleks.append(initializeDalek(doctorPos))
    printAllDalek(daleks)

    while(isAlive):
        hideCursor()
        oldPos = doctorPos
        newPos = playerInput(doctorPos)
        for i in range(len(daleks)):
            clearPosition(daleks[i])
            daleks[i] = moveDalek(daleks[i], newPos)
            printDalek(daleks[i])
            if (list(daleks[i]) == newPos):
                isAlive = False
        clearPosition(oldPos)
        printDoc(newPos)
        doctorPos = newPos

    os.system('cls')
    print("Vous avez perdu!")
    replayInput = input("Voulez vous rejouer? (O/N) : ")
    if replayInput == 'N':
        replay = False