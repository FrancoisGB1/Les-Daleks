from Input import calculateExtremeCoords, clearPosition
from grid import WIDTH, HEIGHT, gotoxy
from random import seed, randint
from util import printScore
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
    collisions = []
    for i in range(len(daleks)):
        for j in range(i+1, len(daleks)):
            if daleks[i] == daleks[j]:
                collisions.append(daleks[i])
    
    return collisions


def killDalek(position, daleks, score):
    indexesToPop = []
    for i in range(len(daleks)):
        if daleks[i] == position:
            indexesToPop.append(i)

    for indexToPop in reversed(indexesToPop): # reversed pour eviter d'utiliser un index hors de la liste
        daleks.pop(indexToPop)
        score += 1
    
    return daleks, score

def DalekCollisionProcess(daleks, ferailles, score):
    collisions = checkCollisionDaleks(daleks)

    for collision in collisions:
        ferailles.append(collision)
        daleks, score = killDalek(collision, daleks, score)
        printScore(score)
    # if collisions != None: 
    #     ferailles.append(collisions)
    #     daleks, score = killDalek(collisions, daleks, score)
    #     gotoxy(0, HEIGHT + 2)
    #     print(f"Score : {score}")

    return score

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

def spawnDalekWave(daleksToSpawn, doctorPos):
    daleks = []
    for i in range(daleksToSpawn):
        daleks.append(initializeDalek(doctorPos))
    return daleks