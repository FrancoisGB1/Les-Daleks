from Input import calculateExtremeCoords, clearPosition
from grid import WIDTH, HEIGHT, gotoxy
from random import seed, randint
from util import printScore
from time import time

seed(time())

def initializeDalek(doctorPos):
    """Initialise la position d'un dalek
    :param doctorPos: Position du docteur afin d'éviter de créer un dalek directement sur le docteur
    :type doctorPos: int
    :return: Coordonnées du dalek à créer
    :rtype: Liste [int, int]
    """
    min_x, min_y, max_x, max_y = calculateExtremeCoords(WIDTH, HEIGHT)
    spawnPoint = [randint(min_x,max_x), randint(min_y, max_y)]
    while spawnPoint == doctorPos: 
        spawnPoint = [randint(min_x,max_x), randint(min_y, max_y)]
    return spawnPoint


def printDalek(position):
    """Affiche à l'écran un dalek
    :param position: Position du docteur afin d'éviter de créer un dalek directement sur le docteur
    :type position: Liste [int, int]
    :return: Aucun
    """
    gotoxy(position[0], position[1])
    print("D")

def printAllDalek(daleks):
    """Affiche à l'écran tous les daleks qui existent
    :param daleks: Position de tous les daleks actuels
    :type daleks: Tableau multidimensionnel [[int, int], ...]
    :return: Aucun
    """
    for dalek in daleks:
        printDalek(dalek)

def clearAllDaleks(daleks):
    """Efface de l'écran tous les daleks qui existent
    :param daleks: Position de tous les daleks actuels
    :type daleks: Tableau multidimensionnel [[int, int], ...]
    :return: Aucun
    """
    for dalek in daleks:
        clearPosition(dalek)

def step_toward(current, target):
    """Détermine l'incrément nécessaire d'une coordonnée x ou y pour atteindre le x ou y ciblé
    :param current: Utilisé pour savoir à quel x ou y on se situe actuellement
    :type current: int
    :param target: Utilisé pour savoir le x ou y où l'on veut se rapprocher
    :type target: int
    :return: L'incrément nécessaire à faire pour se rapprocher du x ou y ciblé
    :rtype: int
    """
    if target > current:
        return 1
    if target < current:
        return -1
    return 0

def moveDalek(dalekPos, doctorPos):
    """
    :param dalekPos: Savoir l'emplacement actuel du dalek à faire bouger
    :type dalekPos: Tableau [int, int]
    :param doctorPos: Savoir la position auquel le dalek doit se rapprocher
    :type doctorPos: Tableau [int, int]
    :return: La nouvelle position du dalek traité après son mouvement
    :rtype: Tableau [int, int]
    """
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
    """Vérifie si un dalek est rentré en collision avec un autre dalek
    :param daleks: Connaître la position de tous les daleks actifs
    :type daleks: Tableau multidimensionnel [[int, int], ...]
    :return: Le ou les endroit(s) où il y a eu une collision
    :rtype: Tableau multidimensionnel [[int, int], ...]
    """
    collisions = []
    for i in range(len(daleks)):
        for j in range(i+1, len(daleks)):
            if daleks[i] == daleks[j]:
                collisions.append(daleks[i])
    
    return collisions


def killDalek(position, daleks, score):
    """
    :param position: Position où il y a un ou des dalek(s) à tuer
    :type position: Tableau [int, int]
    :param daleks: Connaître la position de tous les daleks actifs
    :type daleks: Tableau multidimensionnel [[int, int], ...]
    :param score: Score actuel du joueur représentant le nombre de daleks tués à date
    :type score: int
    :return: La position de tous les daleks sauf ceux qui ont été tués et le nouveau score du joueur après avoir tué x daleks
    :rtype: Tuple ([[int, int], ...], int)
    """
    indexesToPop = []
    for i in range(len(daleks)):
        if daleks[i] == position:
            indexesToPop.append(i)

    for indexToPop in reversed(indexesToPop): # reversed pour eviter d'utiliser un index hors de la liste
        daleks.pop(indexToPop)
        score += 1
    
    return daleks, score

def DalekCollisionProcess(daleks, ferrailles, score):
    """
    :param daleks: Connaître la position de tous les daleks actifs
    :type daleks: Tableau multidimensionnel [[int, int], ...]
    :param position: Position de toutes les ferrailles présentes sur le jeu
    :type position: Tableau multidimensionnel [[int, int], ...]
    :param score: Score actuel du joueur représentant le nombre de daleks tués à date
    :type score: int
    :return: Le nouveau score du joueur après avoir tué x daleks
    :rtype: Tuple ([[int, int], ...], int)
    """
    collisions = checkCollisionDaleks(daleks)

    for collision in collisions:
        ferrailles.append(collision)
        daleks, score = killDalek(collision, daleks, score)
        printScore(score)

    return score

def printAllFerrailles(ferrailles):
    """Affiche à l'écran toutes les ferrailles présentes sur le jeu
    :param ferrailles: Connaître la position de toutes les férailles sur le jeu
    :type ferrailles: Tableau multidimensionnel [[int, int], ...]
    :return: Aucun
    """
    for ferraille in ferrailles:
        gotoxy(ferraille[0], ferraille[1])
        print("F")

def ranIntoFerrailles(dalek, ferrailles):
    """Vérifie si un dalek est entré en collision avec un tas de ferraille
    :param dalek: Position du dalek à traiter
    :type dalek: Tableau [int, int]
    :param ferrailles: Connaître la position de toutes les férailles sur le jeu
    :type ferrailles: Tableau multidimensionnel [[int, int], ...]
    :return: Si un dalek est entré dans un tas de ferraille ou non
    :rtype: boolean
    """
    dalekDied = False
    for ferraille in ferrailles:
        if ferraille == dalek:
            dalekDied = True

    return dalekDied    

def spawnDalekWave(daleksToSpawn, doctorPos):
    """Vérifie si un dalek est entré en collision avec un tas de ferraille
    :param daleksToSpawn: Nombre de daleks à créer
    :type daleksToSpawn: int
    :param doctorPos: Connaître la position actuelle du docteur pour éviter de créer un dalek sur la position du joueur
    :type doctorPos: Tableau [int, int]
    :return: Les positions de tous les daleks créés
    :rtype: Tableau multidimensionnel [[int, int], ...]
    """
    daleks = []
    for i in range(daleksToSpawn):
        daleks.append(initializeDalek(doctorPos))
    return daleks