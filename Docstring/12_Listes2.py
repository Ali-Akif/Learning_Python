#.join(), .split(), __ in __, round(), min(), max()



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

print("Beurre" in liste) #true, attention a la casse

if "Beurre" in courses:
    courses.remove("Beurre")
    print(courses) #

print("Java" in "Javascript") #true

liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]

print(liste[1][0])#Java
print(liste[1][2])#['C']
print(liste[1][-1][0])#C

deuxieme_element = liste[1]
troisieme_element = deuxieme_element[-1]
print(troisieme_element)#C

print(liste[0] [0:2])#

liste.pop(0)
print(liste)#retire python
#remove n'enleve que le premier élément

#les méthodes agissent directement sur les listes sans avoir besoin d'affectation, la ou les fonctions ont besoin d'etre affecté, sinon elles ne retournent rien

#objets muable : listes, disctionnaires, set / immuable : chaines de caracteres, nombre

print(round(2.2))#2
print(round(2.7))#3

print(min([1, 2, 3])) #1
print(max([1,2,3])) #3
print(sum([10, 10, 10])) #30

