minuscules = "une chaine en minuscules"
minuscules = minuscules.upper()
print(minuscules) #sors minuscules écrit en maj
minuscules = minuscules.capitalize()
print(minuscules) #Premiere lettre en maj

espaces = " Voila pleins d'e s p a c e u h "
espaces = espaces.strip()
print(espaces) #retire espace du début et fin de chaine

titre = "introduction"  
titre = titre.upper().center(20)
print(titre)#center ajoute la longueur a celle demandé, en centrant str
