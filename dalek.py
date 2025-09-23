from Input import applyMove, calculateExtremeCoords
from grid import WIDTH, HEIGHT, gotoxy
from random import seed, randint
from time import time

seed(time())

def initializeDalek(doctorPos):
    min_x, min_y, max_x, max_y = calculateExtremeCoords(WIDTH, HEIGHT)
    spawnPoint = [randint(min_x,max_x), randint(min_y, max_y)]
    while spawnPoint == doctorPos: 
        spawnPoint = [randint(min_x,max_x), randint(min_y, max_y)]
    return spawnPoint


def printDalek(position):
    gotoxy(position[0], position[1])
    print("D")

def printAllDalek(daleks):
    for dalek in daleks:
        printDalek(dalek)

def step_toward(current, target):
    if target > current:
        return 1
    if target < current:
        return -1
    return 0

def moveDalek(dalekPos, doctorPos):
    dalekX, dalekY = dalekPos
    doctorX, doctorY = doctorPos

    # Determine meilleur X
    new_x = dalekX + step_toward(dalekX, doctorX)
    # Determine meilleur Y
    new_y = dalekY + step_toward(dalekY, doctorY)

    # Choisir entre faire un mouvement horizontal
    if abs(doctorX - dalekX) > abs(doctorY - dalekY):
        return (new_x, dalekY)   # move horizontally
    else:
        return (dalekX, new_y)   # move vertically
    
def checkCollisionDoctor(dalekPos, doctorPos):
    return dalekPos == doctorPos

    


        


    