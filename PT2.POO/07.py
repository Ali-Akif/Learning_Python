chaine1 = "une poutite chaine"
chaine2 = chaine1.upper()

print(chaine1)

print(chaine2) #logique, on modifie que la chaine 2, la 1 reste en minuscules

liste1 = [1, 5.5, 18]
liste2 = liste1.append(-15)

print(liste1) #liste1 a été modifié mon reuf, c'est pas comme avec chaine

print(liste2)#print none

liste1.insert(2, 'c')  #on insere c a l'indice 2
print(liste1) #print [1, 5.5, 'c', 18, -15], ca décalle l'ancien 2 et s'y insère

liste2 = [8, 9, 10]
liste1.extend(liste2)
print(liste1) # [1, 5.5, 'c', 18, -15, 8, 9, 10]

liste1 = liste1 + liste2
print(liste1) #[1, 5.5, 'c', 18, -15, 8, 9, 10, 8, 9, 10]

liste1 += liste1
print(liste1) #[1, 5.5, 'c', 18, -15, 8, 9, 10, 8, 9, 10, 1, 5.5, 'c', 18, -15, 8, 9, 10, 8, 9, 10] graaave longue la liste frérot