# -*- coding: utf-8 -*-

from random import randrange
from math import ceil

argent = 1000
jeu = True

print("Tu as", argent,"$.")



while jeu:
    

    try:
        n = int(input("Mise sur un chiffre entre 0 et 49 frérot :"))
    except ValueError:
        print("Faut rentrer un chiffre frérot...")
        continue
    if n < 0 or n > 49:
        print("Apprends à lire frère.")
    
    mise = 0

    while mise <= 0 or mise > argent:
        try:
            mise = int(input("Tu veux miser combien ?"))
        except ValueError:
            print("Faut rentrer un chiffre.")
            continue
        if mise > argent:
            print("T'as pas cette somme, t'as", argent,"$.")
        if mise <= 0:
            print("Faut miser un peu quand meme...")
    
    n_gagnant = randrange(50)

    if n == n_gagnant:
        print("Bravo, tu gagnes", mise * 3,"$!!!")
        argent += mise*3
    elif n % 2 == n_gagnant % 2:
        print("Même couleur, tu gagnes la moitié de ta mise, soit", mise * 0.5, "$.")
        mise = ceil(mise * 0.5)
        argent += mise
    else:
        print("Loupé, tu perds ta mise de", mise,"$...")
        argent -= mise  
    
    if argent <= 0:
        print("T'es ruiné, j'tai bien niqué chacal, finito pour toi la partie.")
        jeu = False
    else:
        print("Tu as", argent,"$.")
        quitter = input (" Veux tu quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            jeu = False

input("Appuyez sur Entrée pour quitter...")
    
   