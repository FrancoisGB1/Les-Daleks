import os
from grid import *
from Input import *
from util import *
from dalek import *

# Main
replay = True

while replay:
    score = 0
    isAlive = True
    replayInput = ''
    os.system('cls')
    drawOutline()
    doctorPos = spawnDoc()

    # create 3 daleks to start
    daleks = [initializeDalek(doctorPos)]
    daleks.append(initializeDalek(doctorPos))
    daleks.append(initializeDalek(doctorPos))

    ferailles = []
    printAllDalek(daleks)

    while isAlive:
        hideCursor()
        oldPos = doctorPos

        # player input now returns all three values (will need to update this as we add more parameters, or shove into one list state = [])
        doctorPos, daleks, score = playerInput(doctorPos, daleks, score)

        clearPosition(oldPos)

        score = DalekCollisionProcess(daleks, ferailles, score)

        printAllFerailles(ferailles)
        printDoc(doctorPos)

        clearAllDaleks(daleks)
        for i in reversed(range(len(daleks))):
            daleks[i] = moveDalek(daleks[i], doctorPos)
            if ranIntoFerailles(daleks[i], ferailles):
                daleks.pop(i)
                score += 1
                gotoxy(0, HEIGHT + 2)
                print(f"Score : {score}")
            else:
                printDalek(daleks[i])
                if list(daleks[i]) == doctorPos:
                    isAlive = False

    os.system('cls')
    print("Vous avez perdu!")
    while replayInput.upper() not in ('O', 'N'):
        replayInput = input("Voulez vous rejouer? (O/N) : ")
        if replayInput.upper() == 'N':
            replay = False