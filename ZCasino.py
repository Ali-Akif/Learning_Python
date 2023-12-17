# -*- coding: utf-8 -*-

from random import randrange
from math import ceil

argent = 1000
jeu = True

print("Salut mon reuf, tu commences avec", argent,"$.")

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
    
   