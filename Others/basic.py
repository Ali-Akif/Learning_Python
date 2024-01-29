import random

# Listes d'adjectifs et de noms d'animaux
adjectifs = ["Super", "Mystérieux", "Invisible", "Volant", "Éclair", "Méga", "Fantastique", "Ultimate", "Magique", "Étonnant"]
animaux = ["Chat", "Chien", "Oiseau", "Lion", "Panthère", "Aigle", "Dragon", "Faucon", "Renard", "Loup"]

# Générer un nom de super-héros aléatoire
adjectif = random.choice(adjectifs)
animal = random.choice(animaux)
superhero_name = adjectif + " " + animal

# Afficher le nom de super-héros généré
print("Votre nom de super-héros est :", superhero_name)
