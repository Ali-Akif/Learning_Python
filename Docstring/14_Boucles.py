#for, while

for i in [0, 1, 4, 7, 8]:
    print(i)
# 0
# 1
# 4
# 7
# 8

for lettre in "Python":
    print(lettre)
# P 
# y 
# t 
# h
# o 
# n 
    
for i in range(1000):
    print("Bonjour")
# bonjour
# bonjour
# 1000fois 
    

i = 0
while i < 1000:
    print("bonjour")
    i +=1
#fais la meme chose
    
continuer = "o"

while continuer == "o":
    continuer = input("Voulez vous continuer (o/n) :")

liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        continue
    print(element)