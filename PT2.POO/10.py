chaine ="Bonjour à tous"
print(chaine.split(" "))
#print ['Bonjour', 'à', 'tous']

print(chaine.split())
#la meme

liste = ['Bonjour', 'à', 'tous']
print(" ".join(liste))
#print Bonjour à tous, elle insere ce qu'il y a entre " " entre les éléments

print("hihi".join(liste))
#Bonjourhihiàhihitous..., libre de rajouter des espaces av et ap hihi



def afficher_flottant(flottant):
        if type(flottant) is not float:
            raise TypeError 
        flottant = str(flottant)
        partie_entiere, partie_flottante = flottant.split(".") #crée une liste [ 'partie_entiere', 'partie-flottante']
        return",".join([partie_entiere,partie_flottante[:3]])#joint les éléments de la liste avec "," et en coupant apres la 3 eme de partie flottante
                       
flotteur=3.9090990888

flotteur = afficher_flottant(flotteur)
print(flotteur)
#print 3,909
