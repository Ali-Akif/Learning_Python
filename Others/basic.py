user_input = input("Writes numbers : ")

user_input = [ int(n) for n in user_input.split() ]
new_list = user_input[0]

for i in range(1, len(user_input)):
    new_list += user_input[i]

final = new_list / len(user_input)

print(int(final) if final == int(final) else final)