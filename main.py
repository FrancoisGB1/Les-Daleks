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
    daleks.append(initializeDalek(doctorPos))
    ferailles = []
    printAllDalek(daleks)

    while(isAlive):
        hideCursor()
        oldPos = doctorPos
        newPos = playerInput(doctorPos)
        clearPosition(oldPos)

        DalekCollisionProcess(daleks, ferailles)

        printAllFerailles(ferailles)
        printDoc(newPos)

        clearAllDaleks(daleks)
        for i in reversed(range(len(daleks))):
            daleks[i] = moveDalek(daleks[i], newPos)
            if ranIntoFerailles(daleks[i], ferailles):
                daleks.pop(i)
            else:
                printDalek(daleks[i])
                if (list(daleks[i]) == newPos):
                    isAlive = False
        

        doctorPos = newPos

    os.system('cls')
    print("Vous avez perdu!")
    while replayInput.upper() != 'O' and replayInput.upper() != 'N': 
        replayInput = input("Voulez vous rejouer? (O/N) : ")
        if replayInput.upper() == 'N':
            replay = False