# -*- coding: utf-8 -*-

from random import randrange
from math import ceil

argent = 1000
jeu = True

print("Vous avez", argent,"$.")

while jeu:
    n = -1
    try:
        n = int(input("Sur quelle chiffre voulez vous miser :"))
    except ValueError:
        print("Il faut miser sur un CHIFFRE.")
        continue
    if n < 0 or n > 49:
        print("Il faut rentrer un chiffre entre 0 et 49 l'ami.")
            

