chaine = "Salut les bg"
print(chaine[0])
print(chaine[4])
print(chaine[-1]) #sors le dernier caractere
print(chaine[-4]) #l'indexation se fait a partir de -1 de droite a gauche et de 0 de gauche a droite

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

index_n = alphabet.index("n")

print(alphabet[index_n:])


chaine = "Salut"
print(len(chaine)) #len() pour sortir le nombre de caractere



i = 0

while i < len(chaine):
    print(chaine[i])
    i += 1



presentation = "salut"
print(presentation[0:2]) #a partir du 0, il sors les 2 caractere suivant
print(presentation[2:len(presentation)]) #sors tout a partir de 2


print (presentation[:2]) #pas besoin de spécifier le 0
print (presentation[2:]) #pas besoin du len()

mot ="mite"
mot = "b" + mot[1:]

print(mot)

#count find replace 