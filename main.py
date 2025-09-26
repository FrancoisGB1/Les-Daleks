import os
from grid import *
from Input import *
from util import *
from dalek import *

# Main
replay = True

# LOOP FOR REPLAY ----------------------------
while replay:

    # VARIABLES FOR GAME STATE -----------------------------
    score = 0
    isAlive = True
    newDaleksPerWave = 2 # varie selon la difficulté
    difficulty = 0
    teleportCooldown = 4
    zapCooldown = 4
    # Base game difficulty UI loop and printing the initial game board
    difficulty = difficultyMenu(difficulty)
    os.system('cls')
    drawOutline()
    # Changing the amount of ennemies to spawn based on difficulty chosen
    daleksToSpawn = 3 + difficulty
    # more printing
    doctorPos = spawnDoc()
    # create daleks to start based on difficulty
    daleks = spawnDalekWave(daleksToSpawn, doctorPos)
    ferrailles = []
    printAllDalek(daleks)


    # MAIN GAME LOOP ---------------------------------

    while isAlive:
        # Util function from stack overflow to hide the cursor in game (the cursor was really annoying)
        hideCursor()
        # Daleks respawn once wave is dead
        if not daleks:
            daleksToSpawn += newDaleksPerWave
            daleks = spawnDalekWave(daleksToSpawn,doctorPos)
        # Update the position of the doctor
        oldPos = doctorPos

        # player input now returns all three values (will need to update this as we add more parameters, or shove into one list state = [])
        doctorPos, daleks, score, teleporterCooldown, zapCooldown = playerInput(doctorPos, daleks, score, teleportCooldown, zapCooldown)
        # Clear the board's graphic state
        clearPosition(oldPos)
        # calculating score
        score = DalekCollisionProcess(daleks, ferrailles, score)
        # Re-printing the doctor and obstacles
        printAllFerrailles(ferrailles)
        printDoc(doctorPos)
        # Clearing the Daleks and reprinting them
        clearAllDaleks(daleks)
        for i in reversed(range(len(daleks))):
            daleks[i] = moveDalek(daleks[i], doctorPos)
            if ranIntoFerrailles(daleks[i], ferrailles):
                daleks.pop(i)
                score += 1
                printScore(score)
            else:
                printDalek(daleks[i])
                if list(daleks[i]) == doctorPos:
                    isAlive = False


    # replay loop conditional and final score --------------------------------------------

    print(f"Vous avez perdu! Votre score: {score}")
    replay = replayOrNot()