import numpy as np
import math


class TicTacToe:
    joueur2 = 'O'
    joueur1 = 'X'
    init = '-'

    # affiche les regles  du jeu
    def __init__(self, taille):
        """''Affiche les règles de sélection de l'emplacement"""
        print("Le joueur 1 est matérialisé par X et le joueur 2 est matérialisé par O")
        print("Entrer un de ses nombres pour spécifier la position de votre choix \n")
        k = 0
        for i in range(int(math.sqrt(taille))):
            for j in range(int(math.sqrt(taille))):
                print(str(k).ljust(3), end=" ")
                k += 1
            print()

    # afficher l'echiquier
    @staticmethod
    def show(tab, taille):
        """'Affiche l\'état actuel de l\'échiquier"""
        print("Etat actuel du jeu")
        tabb = np.array(tab).reshape(int(math.sqrt(taille)), int(math.sqrt(taille)))
        for i in range(tabb.shape[0]):
            for j in range(tabb.shape[1]):
                print(str(tabb[i][j]).ljust(3), end=" ")
            print()

    # entrer la valeur dans l'échiquier
    def choice(self, tab, selected, joueur):
        if joueur == 1:
            if tab[selected] == self.init:
                tab[selected] = self.joueur1
                return True
            else:
                return False
        else:
            if tab[selected] == self.init:
                tab[selected] = self.joueur2
                return True
            else:
                return False

    # entrer la taille, l'echiquier, et le joueur
    def win(self, tab, taille, joueur):
        """''Determine si le joueur qui vient de jouer a gagné"""
        element = []
        # read by line
        for i in range(0, taille, int(math.sqrt(taille))):
            for j in range(i, i + int(math.sqrt(taille)), 1):
                element.append(tab[j])
            n1 = int(element.count(self.joueur1))
            n2 = int(element.count(self.joueur2))
            if (joueur == 1) and (n1 == int(math.sqrt(taille))):
                return "gagné"
            elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
                return "gagné"
            element.clear()

        # read by colonne
        for i in range(int(math.sqrt(taille))):
            for j in range(i, taille, int(math.sqrt(taille))):
                element.append(tab[j])
            n1 = int(element.count(self.joueur1))
            n2 = int(element.count(self.joueur2))
            if (joueur == 1) and (n1 == int(math.sqrt(taille))):
                return "gagné"
            elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
                return "gagné"
            element.clear()

        # read by diagonal
        for i in range(0, taille, int(math.sqrt(taille)) + 1):
            element.append(tab[i])
        n1 = int(element.count(self.joueur1))
        n2 = int(element.count(self.joueur2))
        if (joueur == 1) and (n1 == int(math.sqrt(taille))):
            return "gagné"
        elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
            return "gagné"
        element.clear()

        # read by diagonal
        for i in range(int(math.sqrt(taille)) - 1, taille - (int(math.sqrt(taille)) - 1), int(math.sqrt(taille)) - 1):
            element.append(tab[i])
        n1 = int(element.count(self.joueur1))
        n2 = int(element.count(self.joueur2))
        if (joueur == 1) and (n1 == int(math.sqrt(taille))):
            return "gagné"
        elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
            return "gagné"
        element.clear()
