# Fonction pour obtenir un nombre en entrée de l'utilisateur
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Obtenir deux nombres de l'utilisateur
num1 = get_number_input("Entrez le premier nombre : ")
num2 = get_number_input("Entrez le deuxième nombre : ")

# Calculer la somme
somme = num1 + num2

# Afficher le résultat
print(f"La somme de {num1} et {num2} est égale à {somme}.")
