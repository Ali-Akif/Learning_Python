
annee = input("Saisissez une année : ")  
annee = int(annee)   #sinon type annee = str

if annee%4 == 0  :
   print("Votre année est bissextile")
elif annee% 100 == 0 and annee%400 ==0:
   print("Votre année est bissextile")
else:
   print("Votre année n'est pas bissextile")    
    

#In correction, he used a boolean var bissextile assigned with false and worked with it ( if biss % 400 == 0 then its true ) and printed at the end if bissextile print it is else print it's not


content = input("T'es content frérot ? Réponds en binaire bg\n")
content = int(content)  

if content :
   print("hiiiiii il est content")
else:
   print("tocard")      
    
#bonus