#learning "for"

i = 1

while i < 20:
    if i % 3 == 0:
        i += 4
        print("i est incrémenté de 4, i =", i)
        continue
    print("i est égal à ", i)
    i+=1
        