#.join(), .split(),



liste = ["python", "est", "un", "language", "incroyable"]
resultat = "".join(liste)

print(resultat)#pythonestunlanguageincroyable

resultat = "\n".join(liste)
print(resultat)
#python
#est 
#un 
#language
#incroyable

liste = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses = liste.split()
print(courses)#['Riz,', 'Pommes,', 'Lait,', 'Salade,', 'Saumon,', 'Beurre']
#ou
courses = liste.split(", ")
print(courses)#pu de virgule ni d'espaces
