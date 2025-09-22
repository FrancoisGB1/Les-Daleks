from grid import *
import sys
import os

def spawnDoc():
    x, y = calcMiddle()
    gotoxy(x, y)
    print("X", end="", flush=True)
    return [x, y]

def getInput():
    key = msvcrt.getch().decode('utf-8').upper()
    return key

def calculateExtremeCoords(width, height):
    min_x = 2
    min_y = 2
    max_x = width  - 1
    max_y = height - 1
    return min_x, min_y, max_x, max_y


def applyMove(pos, direction):
    # CHANGEMENT: vu que je fais un else dans docMovement qui fait exactement la meme chose, la portion que j'ai enleve est inutile
    # if direction not in MOVES:
    #     return pos  # no change if invalid input
    dx, dy = MOVES[direction]

    min_x, min_y, max_x, max_y = calculateExtremeCoords(WIDTH, HEIGHT) # pour s'assurer que le curseur ne sorte pas des limites
    new_x = pos[0] + dx
    new_y = pos[1] + dy
    if min_x <= new_x <= max_x and min_y <= new_y <= max_y:
        return [new_x, new_y]
    else:
        return pos    # ignore the move if it would leave the border

def playerInput(doctorPos):
    input = getInput()
    # Mouvements possibles pour le joueur
    if(input == 'W'):
        doctorPos = applyMove(doctorPos, "up") 
        return doctorPos
    elif(input == 'A'):
        doctorPos = applyMove(doctorPos, "left")
        return doctorPos
    elif(input == 'S'):
        doctorPos = applyMove(doctorPos, "down")
        return doctorPos
    elif(input == 'D'):
        doctorPos = applyMove(doctorPos, "right")
        return doctorPos
    
    # Autres touches
    elif(input == 'Q'):
        os.system('cls')
        sys.exit()
    else:
        return doctorPos

def prepareMovement(doctorPos):
    gotoxy(doctorPos[0], doctorPos[1])
    print(" ")

def clearPosition(position):
    gotoxy(position[0], position[1])
    print(" ")

def printDoc(position):
    gotoxy(position[0], position[1])
    print("X")