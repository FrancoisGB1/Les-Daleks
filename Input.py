from grid import *
import sys
import os
from random import randint



def spawnDoc():
    """Place le docteur au centre de la grille et l’affiche avec le caractère « X ».

    :return: Position initiale du docteur.
    :rtype: liste [posx, posy]
    """
    x, y = calcMiddle()
    gotoxy(x, y)
    print("X", end="", flush=True)
    return [x, y]


def getInput():
    """Lit une touche pressée par l’utilisateur depuis le clavier 
    et la retourne en majuscule.

    :return: Caractère correspondant à la touche pressée.
    :rtype: str
    """
    key = msvcrt.getch().decode('utf-8').upper()
    return key

def calculateExtremeCoords(width, height):
    """Calcule les coordonnées extrêmes utilisables dans la grille 
    afin d’éviter que le docteur ou les daleks sortent du cadre.

    :param width: Largeur totale de la grille.
    :type width: int

    :param height: Hauteur totale de la grille.
    :type height: int

    :return: Les coordonnées minimales et maximales autorisées 
             (min_x, min_y, max_x, max_y).
    :rtype: tuple (int, int, int, int)
    """
    min_x = 2
    min_y = 2
    max_x = width  - 1
    max_y = height - 1
    return min_x, min_y, max_x, max_y


def applyMove(pos, direction):
    """Applique un déplacement au docteur selon une direction donnée, 
    tout en s'assurant qu'il reste dans les limites de la grille.

    :param pos: Position actuelle du docteur.
    :type pos: liste [posx, posy]

    :param direction: Direction du mouvement ("up", "down", "left", "right").
    :type direction: str

    :return: Nouvelle position du docteur si le mouvement est valide, sinon la position initiale.
    :rtype: liste [posx, posy]
    """
    dx, dy = MOVES[direction]

    min_x, min_y, max_x, max_y = calculateExtremeCoords(WIDTH, HEIGHT)
    new_x = pos[0] + dx
    new_y = pos[1] + dy

    if min_x <= new_x <= max_x and min_y <= new_y <= max_y:
        return [new_x, new_y]
    else:
        return pos


def playerInput(doctorPos, daleks, score):
    """Gère les entrées clavier du joueur pour déplacer le docteur ou utiliser des actions spéciales.

    :param doctorPos: Position actuelle du docteur.
    :type doctorPos: liste [posx, posy]

    :param daleks: Liste des positions actuelles des daleks.
    :type daleks: liste de listes [[posx, posy], ...]

    :param score: Score actuel du joueur.
    :type score: int

    :return: Nouvelle position du docteur, liste mise à jour des daleks et score actualisé.
    :rtype: tuple (liste [posx, posy], liste de listes [[posx, posy], ...], int)
    """
    key = getInput()
    # Movement keys
    if key == 'W':
        doctorPos = applyMove(doctorPos, "up")
    elif key == 'A':
        doctorPos = applyMove(doctorPos, "left")
    elif key == 'S':
        doctorPos = applyMove(doctorPos, "down")
    elif key == 'D':
        doctorPos = applyMove(doctorPos, "right")
    # Other keys
    elif key == 'Q':
        os.system('cls')
        sys.exit()
    elif key == 'Z':
        daleks, score = zapDaleks(daleks, doctorPos, score)
        gotoxy(0, HEIGHT + 2)
        print(f"Score : {score}")
    elif key == 'T':
        doctorPos = teleportDoctor(daleks)  
        return doctorPos, daleks, score

    # Always return updated values
    return doctorPos, daleks, score


def prepareMovement(doctorPos):
    """Efface temporairement l’affichage du docteur à sa position actuelle
    afin de préparer son déplacement.

    :param doctorPos: Position actuelle du docteur.
    :type doctorPos: liste [posx, posy]
    """
    gotoxy(doctorPos[0], doctorPos[1])
    print(" ")


def clearPosition(position):
    """Efface le contenu affiché à une position donnée de la grille.

    :param position: Coordonnées de la case à effacer.
    :type position: liste [posx, posy]
    """
    gotoxy(position[0], position[1])
    print(" ")


def printDoc(position):
    """Affiche le docteur à la position spécifiée en utilisant le caractère « X ».

    :param position: Coordonnées où afficher le docteur.
    :type position: liste [posx, posy]
    """
    gotoxy(position[0], position[1])
    print("X")



def zapDaleks(daleks, doctorPos, score):
    """Zappeur dans le jeu pour tuer tous daleks dans une grid 3x3 autour du docteur
:param daleks: Description du paramètre
:type daleks: liste de listes [[posx, posy], ...]

:param doctorPos: position du docteur
:type: liste [posx, posy]

:param score: compteur pour le score du joueur
:type: int

:return: return survivors, score (retourne les daleks qui ont survécus, et le score selon le nombre tués)
:rtype: 2d array [(posx, posy) ... ] et int
"""

    dx, dy = doctorPos
    min_x, max_x = dx - 1, dx + 1
    min_y, max_y = dy - 1, dy + 1

    survivors = []
    killed = 0
    for d in daleks:
        if min_x <= d[0] <= max_x and min_y <= d[1] <= max_y:
            clearPosition(d)
            killed += 1  # zap it
        else:
            survivors.append(d)

    score += killed
    return survivors, score



def teleportDoctor(daleks):
    """Téléporte le docteur à une position aléatoire sûre dans la grille.
    
    :param daleks: Liste des positions actuelles des daleks.
    :type daleks: liste de listes [[posx, posy], ...]

    :return: Nouvelle position aléatoire du docteur, garantie de ne pas être sur un dalek.
    :rtype: liste [posx, posy]
    """
    min_x, min_y, max_x, max_y = calculateExtremeCoords(WIDTH, HEIGHT)

    while True:
        new_x = randint(min_x, max_x)
        new_y = randint(min_y, max_y)
        newPos = [new_x, new_y]

        # Ensure not colliding with Daleks
        if newPos not in daleks:
            return newPos

def replayOrNot():
    """Validation de si le joueur veut rejouer ou non
    :return: Si le joueur veut rejouer ou non
    :rtype: boolean
    """
    replayInput = ''
    replay = True
    while replayInput.upper() not in ('O', 'N'):
        os.system('cls')
        print("Voulez vous rejouer? (O/N)")
        replayInput = getInput()
        print(replayInput)
        if replayInput.upper() == 'N':
            replay = False    
    
    return replay