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

def moveDalek(dalekPos, doctorPos):
    # left = dalekPos[0] - 1
    # right = dalekPos[0] + 1
    # up = dalekPos[1] + 1
    # down = dalekPos[1] - 1

    # diffLeft = abs(left - doctorPos[0])
    # diffRight= abs(right - doctorPos[0])
    # diffUp = abs(up - doctorPos[1])
    # diffDown = abs(down - doctorPos[1])



    # if diffLeft < diffRight:
    #     optimalX = diffLeft
    # else:
    #     optimalX = diffRight
    
    # if diffUp < diffDown:
    #     optimalY = diffUp
    # else:
    #     optimalY = diffDown
    pass

    


        


    