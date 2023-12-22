#.append(), .extend(), .remove(), liste[::], .index(), .count(), .sort(), .sorted(), .reverse(), .pop(), .clear()



liste = [1, 2, "Python", True]
#list est réservé en python

liste.append("ouii")#ne permet d'ajouter qu'une seule valeur

liste.extend([10, 25, 30])

liste.remove(1)

print(liste)
#[2, 'Python', True, 'ouii', 10, 25, 30]
# 0   1          2     3      4   5   6
# -7   -6        -5    -4     -3  -2 -1 

liste =["Utilisateur_01",
        "Utilisateur_02",
        "Utilisateur_03",
        "Utilisateur_04",
        "Utilisateur_05",
        "Utilisateur_06"]

print(liste[0:1]) #['Utilisateur_1']
print(liste[0:2]) #['Utilisateur_01', 'Utilisateur_02']
print(liste[1:2]) #['Utilisateur_02']
print(liste[:]) #['Utilisateur_01', 'Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04', 'Utilisateur_05', 'Utilisateur_06']
print(liste[:-1])#['Utilisateur_01', 'Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04', 'Utilisateur_05']
print(liste[:-2])#['Utilisateur_01', 'Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04']
print(liste[::2])#['Utilisateur_01', 'Utilisateur_03', 'Utilisateur_05'] pas de 2
print(liste[1::2])#['Utilisateur_02', 'Utilisateur_04', 'Utilisateur_06']
print(liste[1:-2:2])#['Utilisateur_02', 'Utilisateur_04']
print(liste[::-1])#['Utilisateur_06', 'Utilisateur_05', 'Utilisateur_04', 'Utilisateur_03', 'Utilisateur_02', 'Utilisateur_01']

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
resultat = employes.index("Max")#sors la position de l'élément
print(resultat)#1

resultat = employes.count("Max")
print(resultat)#2

resultat=employes.sort()
print(employes) #['Alex', 'Carlos', 'Martine', 'Max', 'Max', 'Patrick'] trié dans l'ordre alphabétique, sort() retourne none, print resultat = none

employes = sorted(employes)
print(employes)#sorted est une fonction, qui renvoi la liste trié contrairement a sort

employes.reverse()
print(employes)#['Patrick', 'Max', 'Max', 'Martine', 'Carlos', 'Alex'] inverse tout les elements de la liste


element = employes.pop(-1)
print(element)#Alex a été enlevé de la liste et a été ajouté a element

employes.clear()
print(employes)#[], vide entierement la liste et renvoi r


