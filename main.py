import os
from grid import *
from movement import *

# Main
os.system('cls')
drawOutline()
doctorPos = spawnDoc()

while(1):
    oldPos = doctorPos
    newPos = docMovement(doctorPos)
    clearPosition(oldPos)
    printDoc(newPos)
    doctorPos = newPos