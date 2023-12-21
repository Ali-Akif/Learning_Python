# a = input("Entrez un premier nombre : ")
# b = input("Entrez un deuxieme nombre : ")

# if a.isdigit() and b.isdigit():
#     print(f"Le résultat de votre addition est {int(a) + int(b)}")
# else:
#     print("Veuillez entrez des nombres")

a = b = ""

while not (a.isdigit() and b.isdigit()):  #sans les parenthese: while not a.isdigit() and not b.isdigit()
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition de {a} et {b} est égal à {int(a) + int(b)}")
