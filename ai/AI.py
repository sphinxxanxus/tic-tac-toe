import math


class AI:
    joueur1 = 'X'  # AI
    joueur2 = 'O'  # Human Player
    init = '-'
    availabledeplacement = []

    def __init__(self):
        return

    def deplacementavailable(self, tab):
        """'Get the list index of deplacement available"""
        for i in range(len(tab)):
            if tab[i] == self.init:
                self.availabledeplacement.append(i)

    def evaluate(self, tab, taille, joueur)->int:
        """''Determine si le joueur qui vient de jouer a gagné"""
        element = []
        # read by line
        for i in range(0, taille, int(math.sqrt(taille))):
            for j in range(i, i + int(math.sqrt(taille)), 1):
                element.append(tab[j])
            n1 = int(element.count(self.joueur1))
            n2 = int(element.count(self.joueur2))
            if (joueur == 1) and (n1 == int(math.sqrt(taille))):
                return 10
            elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
                return -10
            element.clear()

        # read by colonne
        for i in range(int(math.sqrt(taille))):
            for j in range(i, taille, int(math.sqrt(taille))):
                element.append(tab[j])
            n1 = int(element.count(self.joueur1))
            n2 = int(element.count(self.joueur2))
            if (joueur == 1) and (n1 == int(math.sqrt(taille))):
                return 10
            elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
                return -10
            element.clear()

        # read by diagonal
        for i in range(0, taille, int(math.sqrt(taille)) + 1):
            element.append(tab[i])
        n1 = int(element.count(self.joueur1))
        n2 = int(element.count(self.joueur2))
        if (joueur == 1) and (n1 == int(math.sqrt(taille))):
            return 10
        elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
            return -10
        element.clear()

        # read by diagonal
        for i in range(int(math.sqrt(taille)) - 1, taille - (int(math.sqrt(taille)) - 1), int(math.sqrt(taille)) - 1):
            element.append(tab[i])
        n1 = int(element.count(self.joueur1))
        n2 = int(element.count(self.joueur2))
        if (joueur == 1) and (n1 == int(math.sqrt(taille))):
            return 10
        elif (joueur == 2) and (n2 == int(math.sqrt(taille))):
            return -10
        element.clear()
        return 0

    def minmax(self, tab, depth,  is_max)->int:
        taille = len(tab)
        if is_max:
            joueur = 1
        else:
            joueur = 2

        score = int(self.evaluate(tab, taille, joueur))
        if score == -10:
            return score
        elif score == 10:
            return score
        elif taille > 9:
            if depth == 8:
                return score
            elif depth == 4:
                return score
        self.deplacementavailable(tab)
        # Deplacement possible
        if len(self.availabledeplacement) == 0:
            return 0
        self.availabledeplacement.clear()
        # branch AI
        if is_max:
            is_max = False
            best = -1000
            for i in range(taille):
                if tab[i] == self.init:
                    tab[i] = self.joueur1
                    best = max(best, int(self.minmax(tab, depth+1, is_max)))
                    tab[i] = self.init
            return best

        # Branch adversaire
        best = 1000
        is_max = True
        for j in range(taille):
            if tab[j] == self.init:
                tab[j] = self.joueur2
                best = min(best, int(self.minmax(tab, depth+1, is_max)))
                tab[j] = self.init
        return int(best)

    def findbestmove(self, tab):
        global move
        bestval = -1000
        for i in range(len(tab)):
            if tab[i] == self.init:
                tab[i] = self.joueur1
                moveval = int(self.minmax(tab, 0, False))
                tab[i] = self.init
                if moveval > bestval:
                    move = i
                    bestval = moveval
        return int(move)
