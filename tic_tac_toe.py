#!/usr/bin/python3
from ai import tictacoe
from ai import AI
from random import randint

print('#######        #######              #######        ###\n' +
      '   #   #   ###    #    ###     ###     #    ###   #   #\n' +
      '   #      #       #   #   #   #        #   #   #  ####\n' +
      '   #   #  #       #   #   ##  #        #   #   #  #\n' +
      '   #   #   ###    #    ##  ##  ###     #    ###    ####\n')
menu: int = 0
n: int = 0
try:
    while (menu <= 0) or (menu > 2):
        menu = int(input("Contre ordinateur ".upper().ljust(10) + "1\n"
                         + "Jouer à deux ".upper().ljust(10)
                         + "2 ".ljust(10)))
    n = int(input("Entrer la taille du jeu!!! \nPar exemple si c'est 3*3 entrer 3: "))
except ValueError:
    print()
if n <= 2:
    n = 3

n *= n  # nombre d'élément dans le jeu
tic =tictacoe.TicTacToe(n)  # initialisation de la class
ai = AI.AI()
echiquier = ['-'] * n  # initialisation de l'echiquier
tic.show(echiquier, n)  # show stage of game
deplacement = 0  # nombre de deplacement
player = randint(1, 2)  # numero du joueur
if menu == 1:  # case game within AI and Human
    while deplacement < n:
        try:
            if player == 1:  # tour of AI
                print("C'est votre tour ordinateur")
                choix = ai.findbestmove(echiquier)
            else:  # tour of Human player
                print("C'est votre tour joueur {}".format(str(player)))
                choix = int(input("Entrer la position de votre choix : "))

            if choix < 0 or choix > n - 1:  # verification de choix
                print("Le choix doit entre compris entre les nombres specifiés")
            elif tic.choice(echiquier, choix, player):  # set the choice position
                tic.show(echiquier, n)  # show the game stage
                if tic.win(echiquier, n, player) == "gagné":  # verify if player win or not
                    print("Bravo ^_^ !!! Joueur {} a gagné".format(player))
                    exit()
                deplacement += 1  # increment the number of deplacement
                if player == 1:
                    player = 2
                else:
                    player = 1
            else:
                print("L'emplacement entré est déja utilisé")
        except ValueError:
            print("Entrer les valeurs specifiées dans la règle du jeu")
else:  # case game within two humans
    while deplacement < n:
        try:
            print("C'est votre tour joueur {}".format(str(player)))  # get choice of player
            choix = int(input("Entrer la position de votre choix : "))
            if choix < 0 or choix > n - 1:
                print("Le choix doit entre compris entre les nombres specifiés")
            elif tic.choice(echiquier, choix, player):  # set the choice position
                tic.show(echiquier, n)  # show game stage
                if tic.win(echiquier, n, player) == "gagné":  # verify if player win or not
                    print("Bravo ^_^ !!! Joueur {} a gagné".format(player))
                    exit()
                deplacement += 1
                if player == 1:
                    player = 2
                else:
                    player = 1
            else:
                print("L'emplacement entré est déja utilisé")
        except ValueError:
            print("Entrer les valeurs specifiées dans la règle du jeu")
print("Désolé °_° !!! Match nul")
