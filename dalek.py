from Input import calculateExtremeCoords, clearPosition
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

def clearAllDaleks(daleks):
    for dalek in daleks:
        clearPosition(dalek)

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
        return (new_x, dalekY)   # bouge horizontalement
    else:
        return (dalekX, new_y)   # bouge verticalement
        

def checkCollisionDaleks(daleks):
    for i in range(len(daleks)):
        for j in range(i+1, len(daleks)):
            if daleks[i] == daleks[j]:
                return daleks[i]
    
    return None

def killDalek(position, daleks):
    indexesToPop = []
    for i in range(len(daleks)):
        if daleks[i] == position:
            indexesToPop.append(i)

    for indexToPop in reversed(indexesToPop): # reversed pour eviter d'utiliser un index hors de la liste
        daleks.pop(indexToPop)
    
    return daleks

def DalekCollisionProcess(daleks, ferailles):
    collision = checkCollisionDaleks(daleks)
    if collision != None: 
        ferailles.append(collision)
        daleks = killDalek(collision, daleks)

def printAllFerailles(ferailles):
    for feraille in ferailles:
        gotoxy(feraille[0], feraille[1])
        print("F")

def ranIntoFerailles(dalek, ferailles):
    dalekDied = False
    for feraille in ferailles:
        if feraille == dalek:
            dalekDied = True

    return dalekDied    