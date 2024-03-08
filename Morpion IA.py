# ici on créer la fenetre
import numpy as np
from random import *



def vérifWin(matrice):
    """
    fonction qui vérifie, si il y a une win dans la matrice rentré en paramétre,
    si oui, qui c'est, si il y a une égalité ou si il passe au tour suivant
    :param : matrice de jeu
    :return: chaine de caractère, de qui est le gagnant, égalité ou si on passe au tour d'après
    """
    for i in range(len(matrice)):
        if matrice[i][0] == matrice[i][1] and matrice[i][1] == matrice[i][2]:  # vérifie les lignes
            if matrice[i][0] == 1:
                return "le joueur 1 à gagner"
            elif matrice[i][0] == 2:
                return "le joueur 2 à gagner"

        elif matrice[0][i] == matrice[1][i] and matrice[1][i] == matrice[2][i]:  # vérifit les colones
            if matrice[0][i] == 1:
                return "le joueur 1 à gagner"
            elif matrice[0][i] == 2:
                return "le joueur 2 à gagner"

    if matrice[0][0] == matrice[1][1] and matrice[1][1] == matrice[2][2]:  # vérifit la diagonal de gauche à droite
        if matrice[0][0] == 1:
            return "le joueur 1 à gagner"
        elif matrice[0][0] == 2:
            return "le joueur 2 à gagner"

    elif matrice[0][2] == matrice[1][1] and matrice[1][1] == matrice[2][0]:  # vérifit le diagonal de droite à gauche
        if matrice[0][2] == 1:
            return "le joueur 1 à gagner"
        elif matrice[0][2] == 2:
            return "le joueur 2 à gagner"

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 0:
                return "Au joueur suivant"  # sinon si il reste des cases vides alors c'est à l'autre joueur

    return "Egalité"  # si plus de cases vide alors égalité


global joueur
joueur = 0
def majMatrice(cases, matrice):
    """
    function qui met à jour le matrice de jeu
    :param cases: entier du numéro de la case qui à était jouée
    :param matrice: la matrice de jeu
    :return: la matrice mis a jour
    """
    global joueur
    match cases :
        case 1:
            if joueur % 2 == 0:
                matrice[0, 0] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[0, 0] = 2
                joueur += 1
                return matrice
        case 2:
            if joueur % 2 == 0:
                matrice[0, 1] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[0, 1] = 2
                joueur += 1
                return matrice
        case 3:
            if joueur % 2 == 0:
                matrice[0, 2] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[0, 2] = 2
                joueur += 1
                return matrice
        case 4:
            if joueur % 2 == 0:
                matrice[1, 0] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[1, 0] = 2
                joueur += 1
                return matrice
        case 5:
            if joueur % 2 == 0:
                matrice[1, 1] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[1, 1] = 2
                joueur += 1
                return matrice
        case 6:
            if joueur % 2 == 0:
                matrice[1, 2] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[1, 2] = 2
                joueur += 1
                return matrice
        case 7:
            if joueur % 2 == 0:
                matrice[2, 0] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[2, 0] = 2
                joueur += 1
                return matrice
        case 8:
            if joueur % 2 == 0:
                matrice[2, 1] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[2, 1] = 2
                joueur += 1
                return matrice
        case 9:
            if joueur % 2 == 0:
                matrice[2, 2] = 1
                joueur += 1
                return matrice
            elif joueur % 2 == 1:
                matrice[2, 2] = 2
                joueur += 1
                return matrice

def morpion ():
    """
    function pour jouer au morpion en console, sois 1vs1 en local, sois contre IA simple (qui joue aléatoirement),
    sois IA moyenne (contre l'adversaire, sinon joue aléatoirement), sois IA avancée (joue les coup gagnant,
    sinon contre adversaire, sinon joue aléatoirement), sois 1vs1 en réseau.
    :return: chaque tour met en console le matrice de jeu
    """
    mj = np.zeros((3,3))
    compteur = 0
    choix = int(input(f'1 : 1vs1 en local \n2 : IA niveau simple \n3 : IA niveau moyen \n4 : IA niveau avancée'))
    ligne = int(input("Quel ligne ? "))
    colonne = int(input("Quel colonne ?"))
    while True :
        if compteur % 2 == 0:
            while mj[ligne, colonne] == 1 or mj[ligne, colonne] == 2 :
                ligne = int(input("Quel ligne ? "))
                colonne = int(input("Quel colonne ?"))
            mj[ligne, colonne] = 1
            win = vérifWin(mj)
            compteur+=1
            if win == "le joueur 1 à gagner":
                print(mj)
                return(win)  # si joueur 1 à gagner, arrête le jeu et print que le joueur 1 à gagner
            elif win == "Egalité":
                print(mj)
                return(win) # si égalité, arrête le jeu et print égalité
            else:
                print(mj)
                print(win)  # print que c'est au joueur suivant"
        elif compteur % 2 == 1 :
            if choix == 1 :
                ligne = int(input("Quel ligne ? "))
                colonne = int(input("Quel colonne ?"))
                while mj[ligne, colonne] == 1 or mj[ligne, colonne] == 2:
                    ligne = int(input("Quel ligne ? "))
                    colonne = int(input("Quel colonne ?"))
                mj[ligne, colonne] = 2
            elif choix == 2:
                ligne = randint(0, 2)
                colonne = randint(0, 2)
                while mj[ligne, colonne] == 1 or mj[ligne, colonne] == 2:
                    ligne = randint(0, 2)
                    colonne = randint(0, 2)
                mj[ligne, colonne] = 2
            elif choix == 3:
                test = "true"
                for i in range(3):
                    if mj[i, 0] == mj[i, 1] == 1:
                        if mj[i, 2] != 1 and mj [i, 2] != 2 :
                            mj[i, 2] = 2
                            test = "false"
                            break
                    elif mj[i, 1] == mj[i, 2] == 1:
                        if mj[i, 0] != 1 and mj[i, 0] != 2:
                            mj[i, 0] = 2
                            test = "false"
                            break
                    elif mj[i, 0] == mj[i, 2] == 1:
                        if mj[i, 1] != 1 and mj[i, 1] != 2:
                            mj[i, 1] = 2
                            test = "false"
                            break
                    elif mj[0, i] == mj[1, i] == 1:
                        if mj[2, i] != 1 and mj[2,i] != 2 :
                            mj[2, i] = 2
                            test = "false"
                            break
                    elif mj[1, i] == mj[2, i] == 1:
                        if mj[0, i] != 1 and mj[0, i] != 2:
                            mj[0,i] = 2
                            test = "false"
                            break
                    elif mj[0, i] == mj[2, i] == 1:
                        if mj[1, i] != 1 and mj[1,i] != 2:
                            mj[1, i] = 2
                            test = "false"
                            break
                    elif mj[0, 0] == mj[1,1] == 1:
                        if mj[2, 2] != 1 and mj[2,2] != 2:
                            mj[2,2] = 2
                            test = "false"
                            break
                    elif mj[2, 2] == mj[1,1] == 1:
                        if mj[0, 0] != 1 and mj[0,0] != 2:
                            mj[0,0] = 2
                            test = "false"
                            break
                    elif mj[0, 0] == mj[2,2] == 1:
                        if mj[1, 1] !=  1 and mj[1, 1] != 2:
                            mj[1,1] = 2
                            test = "false"
                            break
                    elif mj[0, 2] == mj[1,1] == 1:
                        if mj[2, 0] != 2 and mj[2, 0] != 1:
                            mj[2,0]=2
                            test = "false"
                            break
                    elif mj[2, 0] == mj[1,1] == 1:
                        if mj[0, 2] != 1 and mj[0, 2] != 2:
                            mj[0, 2] = 2
                            test = "false"
                            break
                    elif mj[0, 2] == mj[2,0] == 1:
                        if mj[1, 1] != 2 and mj[1,1]:
                            mj[1,1] = 2
                            test = "false"
                            break
                if test == "true":
                    ligne = randint(0, 2)
                    colonne = randint(0, 2)
                    while mj[ligne, colonne] == 1 or mj[ligne, colonne] == 2:
                        ligne = randint(0, 2)
                        colonne = randint(0, 2)
                    mj[ligne, colonne] = 2
            if choix == 4 :
                test = "true"
                for i in range(3):
                    if mj[i, 0] == mj[i, 1] == 2:
                        if mj[i, 2] != 1 and mj [i, 2] != 2 :
                            mj[i, 2] = 2
                            test = "false"
                            break
                    elif mj[i, 1] == mj[i, 2] == 2:
                        if mj[i, 0] != 1 and mj[i, 0] != 2:
                            mj[i, 0] = 2
                            test = "false"
                            break
                    elif mj[i, 0] == mj[i, 2] == 2:
                        if mj[i, 1] != 1 and mj[i, 1] != 2:
                            mj[i, 1] = 2
                            test = "false"
                            break
                    elif mj[0, i] == mj[1, i] == 2:
                        if mj[2, i] != 1 and mj[2,i] != 2 :
                            mj[2, i] = 2
                            test = "false"
                            break
                    elif mj[1, i] == mj[2, i] == 2:
                        if mj[0, i] != 1 and mj[0, i] != 2:
                            mj[0,i] = 2
                            test = "false"
                            break
                    elif mj[0, i] == mj[2, i] == 2:
                        if mj[1, i] != 1 and mj[1,i] != 2:
                            mj[1, i] = 2
                            test = "false"
                            break
                    elif mj[0, 0] == mj[1,1] == 2:
                        if mj[2, 2] != 1 and mj[2,2] != 2:
                            mj[2,2] = 2
                            test = "false"
                            break
                    elif mj[2, 2] == mj[1,1] == 2:
                        if mj[0, 0] != 1 and mj[0,0] != 2:
                            mj[0,0] = 2
                            test = "false"
                            break
                    elif mj[0, 0] == mj[2,2] == 2:
                        if mj[1, 1] !=  1 and mj[1, 1] != 2:
                            mj[1,1] = 2
                            test = "false"
                            break
                    elif mj[0, 2] == mj[1,1] == 2:
                        if mj[2, 0] != 2 and mj[2, 0] != 1:
                            mj[2,0]=2
                            test = "false"
                            break
                    elif mj[2, 0] == mj[1,1] == 2:
                        if mj[0, 2] != 1 and mj[0, 2] != 2:
                            mj[0, 2] = 2
                            test = "false"
                            break
                    elif mj[0, 2] == mj[2,0] == 2:
                        if mj[1, 1] != 2 and mj[1,1]:
                            mj[1,1] = 2
                            test = "false"
                            break
                if test == "true":
                    for j in range(3):
                        if mj[j, 0] == mj[j, 1] == 1:
                            if mj[j, 2] != 1 and mj [j, 2] != 2 :
                                mj[j, 2] = 2
                                test = "false"
                                break
                        elif mj[j, 1] == mj[j, 2] == 1:
                            if mj[j, 0] != 1 and mj[j, 0] != 2:
                                mj[j, 0] = 2
                                test = "false"
                                break
                        elif mj[j, 0] == mj[j, 2] == 1:
                            if mj[j, 1] != 1 and mj[j, 1] != 2:
                                mj[j, 1] = 2
                                test = "false"
                                break
                        elif mj[0, j] == mj[1, j] == 1:
                            if mj[2, j] != 1 and mj[2,j] != 2 :
                                mj[2, j] = 2
                                test = "false"
                                break
                        elif mj[1, j] == mj[2, j] == 1:
                            if mj[0, j] != 1 and mj[0, j] != 2:
                                mj[0,j] = 2
                                test = "false"
                                break
                        elif mj[0, j] == mj[2, j] == 1:
                            if mj[1, j] != 1 and mj[1,j] != 2:
                                mj[1, j] = 2
                                test = "false"
                                break
                        elif mj[0, 0] == mj[1,1] == 1:
                            if mj[2, 2] != 1 and mj[2,2] != 2:
                                mj[2,2] = 2
                                test = "false"
                                break
                        elif mj[2, 2] == mj[1,1] == 1:
                            if mj[0, 0] != 1 and mj[0,0] != 2:
                                mj[0,0] = 2
                                test = "false"
                                break
                        elif mj[0, 0] == mj[2,2] == 1:
                            if mj[1, 1] !=  1 and mj[1, 1] != 2:
                                mj[1,1] = 2
                                test = "false"
                                break
                        elif mj[0, 2] == mj[1,1] == 1:
                            if mj[2, 0] != 2 and mj[2, 0] != 1:
                                mj[2,0]=2
                                test = "false"
                                break
                        elif mj[2, 0] == mj[1,1] == 1:
                            if mj[0, 2] != 1 and mj[0, 2] != 2:
                                mj[0, 2] = 2
                                test = "false"
                                break
                        elif mj[0, 2] == mj[2,0] == 1:
                            if mj[1, 1] != 2 and mj[1,1]:
                                mj[1,1] = 2
                                test = "false"
                                break
                if test == "true":
                    ligne = randint(0, 2)
                    colonne = randint(0, 2)
                    while mj[ligne, colonne] == 1 or mj[ligne, colonne] == 2:
                        ligne = randint(0, 2)
                        colonne = randint(0, 2)
                    mj[ligne, colonne] = 2
            win = vérifWin(mj)
            compteur += 1
            if win == "le joueur 2 à gagner":
                print(mj)
                return ("L'IA à gagner")  # si l'IA à gagner, arrête le jeu et print que l'IA à gagner
            elif win == "Egalité":
                print(mj)
                return (win)  # si égalité, arrête le jeu et print égalité
            else:
                print(mj)
                print(win)  # print que c'est au joueur suivant"