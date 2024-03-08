# ici on créer la fenetre
from tkinter import *
from tkinter.messagebox import *
import numpy as np






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
    fonction qui vérifie, si il y a une win dans la matrice rentré en paramétre,
    si oui, qui c'est, si il y a une égalité ou si il passe au tour suivant
    :param : matrice de jeu
    :return: chaine de caractère, de qui est le gagnant, égalité ou si on passe au tour d'après
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
