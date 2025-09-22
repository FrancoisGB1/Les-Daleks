import os 
import msvcrt

WIDTH = 32
HEIGHT = 16

doctorPos = [0, 0]

MOVES = {
    "up":    (0, -1),
    "down":  (0,  1),
    "left":  (-1, 0),
    "right": (1,  0),
}

#Gemini google code
def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')


def drawOutline():
    # top and bottom borders
    for x in range(1, WIDTH + 1):
        gotoxy(x, 1)
        print("-", end="")
        gotoxy(x, HEIGHT)
        print("-", end="")
    # left and right borders
    for y in range(2, HEIGHT):  # skip corners
        gotoxy(1, y)
        print("|", end="")
        gotoxy(WIDTH, y)
        print("|", end="")

def calcMiddle():
    x = WIDTH // 2
    y = HEIGHT // 2
    return x, y

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

def docMovement(doctorPos):
    move = getInput()
    if(move == 'W'):
        doctorPos = applyMove(doctorPos, "up") 
        return doctorPos
    elif(move == 'A'):
        doctorPos = applyMove(doctorPos, "left")
        return doctorPos
    elif(move == 'S'):
        doctorPos = applyMove(doctorPos, "down")
        return doctorPos
    elif(move == 'D'):
        doctorPos = applyMove(doctorPos, "right")
        return doctorPos
    else:
        return doctorPos

def prepareDocMovement(doctorPos):
    gotoxy(doctorPos[0], doctorPos[1])
    print(" ")

def clearDoc(position):
    gotoxy(position[0], position[1])
    print(" ")

def printDoc(position):
    gotoxy(position[0], position[1])
    print("X")


# Main
os.system('cls')
drawOutline()
doctorPos = spawnDoc()

while(1):
    oldPos = doctorPos
    newPos = docMovement(doctorPos)
    clearDoc(oldPos)
    printDoc(newPos)
    doctorPos = newPos