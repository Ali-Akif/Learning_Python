# random.randint.uniform.randrange.   dir,  os.path.dirname,  os.path.exists,  os.makedirs,  os.removedirs,  help(), pprint()



import random
import os
from pprint import pprint
r = random.randint(0, 2)
print(r) #print random entre 0, 2

r = random.uniform(0,1)
print(r) #0.7290564517735932

r = random.randrange(999)
print(r)#113, 999 est exclu, si on fait 1 ca sortira toujours 0

r = random.randrange(0, 101, 10) #de 0 a 100 avec un pas de 10
print(r)#70

chemin = os.path.dirname(__file__)
print(chemin)
dossier = os.path.join(chemin, "dossier", "test")#gère automatiquement les slash, utile pour marcher sur windows, mac et linux
print(dossier)
if not os.path.exists(dossier):
    os.makedirs(dossier) #mkdir ne peut pas créer plusieurs dossiers

# ou os.makedirs(dossier, exist_ok=True)

if os.path.exists(dossier):
    os.removedirs(dossier)


print(dir(random)) #tout ce qui a __nom__ on touche pas, c'est ce que le module utilise

help(random.randint) #donne info sur fonction

pprint(dir(random))#sors les données de facon plus lisible, utilisable sur pleins de trucs