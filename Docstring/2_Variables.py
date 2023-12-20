nombre = 5
#nom   #objet
nombre_2 = 5
#on ne crée pas de nouvel objet, on pointe vers le meme objet (int 5)

print(id(nombre))
#140736571456056

#id() pour l'emplacement d'une variable

a = 8 #affecation simple
a, b, c = 5, 8, 9 #affecations parrallèles 
a = b = c = 5 #affectations multiples

id(True) #Singleton, toujours le meme emplacement
id(500) # change a chaque fois
id(5) #ne change pas, il attribue en singleton pour -5 a 256


#les règles de nommage
    #ne peux pas commencer par un chiffre
    #pas d'espaces
    #que des caracteres alpha numeriques, nb de 0 a 9 et _
    #certains mot reservé, break, True

#convention de nommage
    #full minuscule, mot séparé par _

#50 est différent de "50"
#50 + "50" ne marche pas car python est fortement typé, contrairement à Jvscript
a = "5"
b = 10
a = int(a)
print(a + b)
print(type(a)) #class 'int'


a = "J'ai une classe de " + str(30) + " élèves"
b = str(10) + " + " + "5" + " est égal à " + str(15)
c = 10 + int("5")
d = "L'addition de 10 + 5 est égal à " + str(10 + 5)
print(a)
print(b)
print(c)
print(d)

nombre = input("Entrez un nombre: ")
print(nombre)



