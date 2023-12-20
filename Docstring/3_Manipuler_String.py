b = "bOnjour tout le monde"
print(b.upper())
    #BONJOUR TOUT LE MONDE
print(b.lower())
    #bonjour tout le monde
print(b.capitalize())
    #Bonjour tout le monde
print(b.title())
    #Bonjour Tout Le Monde

b = b.replace("jour","soir")
print(b)
    #bOnsoir tout le monde
b = b.replace(" ", "").replace("o", "oo")
print(b)
    #bOnsooirtooutlemoonde
b = " bonjour "
b = b.strip()
print(b)
    #'bonjour'
b = b.strip("ujor")
print(b)
    #'bon'
b = " bonjour "
b = b.rstrip(" ujor")
    #' bon'
b = " bonjour "
b = b.lstrip(" ujor")
    #'bonjour '

suite = " 1, 2, 3, 4, 5".split(", ")
print(suite)
#[' 1', '2', '3', '4', '5']
suite = ", ".join(suite)
print(suite)
#1, 2, 3, 4, 5
# on peut join avec "." et ça ferait 1.2.3.4.5
#on ne peut pas join() des éléments qui ne sont pas str

print("9".zfill(4))
#0009
print("9".zfill(3))
#009

for i in range(100):
    print(i)
    #1 
    #2...
    #99

for i in range(100):
    print(str(i).zfill(3))  #zfill() ne marche qu'avec des string
    #001
    #002..
    #099

b = "bonjour"
print(b.islower())
#True

print(b.istitle())
#False

b = "50"
print(b.isdigit())
#True

b ="50t"
print(b.isdigit())
#False

if b.isdigit():
    print("b")
else:
    print("boo")
    #print boo

b = "bonjour le jour".count("jour")
print(b)
    #2
b = "bonjour le jour".count(" jour")
print(b)
    #1
b = "bonjour le jour".count(" jour") + "bonjour le jour".count("le")
print(b)
    #2, on peut pas enchaine les .count comme avec .replace
b = "Bonjour le jour"
print(b.find("jour"))
    #3, car B 0 o 1 n 2 Jour est situé sur l'index 3
print(b.index("jour"))
    #3 pareil
print(b.rfind("jour"))
    #11, on compte toujours de gauche a droite mais on cherche la premiere occurence depus la droite

b = "image.png"
print(b.endswith(".png"))
    #True
print(b.startswith("image"))