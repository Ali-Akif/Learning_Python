# -*- coding: utf-8 -*-

from random import randrange
from math import ceil

argent = 1000
jeu = True

print("Tu commences avec", argent,"$.")

while jeu:
    n = -1 #sinon on sors jamais de la boucle try
    while n == -1:
        try:
            n = int(input("Sur quelle chiffre tu veux miser ?"))
        except ValueError:
            print("Rentre un chiffre gros...")
            continue
        if n < 0 or n > 49:
            print("Faut rentrer un chiffre entre 0 et 49...")
            
    if 0 <= n <= 49: #Ne doit surtout pas etre placé au meme niveau que try, sinon jeu passera direct a la suite dans rentrer de mise, et la c'est la cata frérot, cela dit il doit etre placé au meme niveau que while, pour que while puisse le prendre en compte 
        mise = 0
        while mise <= 0:
            try:
                mise = int(input("Tu veux miser combien ? "))
            except ValueError:
                print("Rentre un chiffre gros...")
                continue
            if mise <= 0:
                print("Faut miser un peu quand meme !")
            elif mise > argent:
                print("T'as ça toi ? Tu as", argent,"$ je te rappelle !")

    n_gagnant = randrange(50)
    print("La roue tourne...")
    print("C'est le numéro", n_gagnant,"!")

    if n == n_gagnant:
        mise += mise * 3
        print("Bravo, t'as gagné", mise,"$!!!")
        argent += mise
    elif n % 2 == n_gagnant % 2:
        mise = ceil(mise * 0.5)
        print("Bonne couleur, t'as gagné", mise,"$!")
        argent += mise
    else:
        print("Pas de chance, tu as perdu", mise,"$...")
        argent -= mise

    if argent <= 0:
        jeu = False
        print("t'as pu de thune")
    
    if argent > 0:
        print("Tu as désormais", argent,"$.")
        continuer_jeu = input("Tu veux continuer la partie ? (o/n)")
    if continuer_jeu == "n" or continuer_jeu == "N":
        jeu = False
        print("Bye bye...")


input("Appuie sur entrée pour quitter...")
    

        
        