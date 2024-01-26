user_choice = 0

while user_choice not in [ "1", "2"]:
    user_choice = input("Fahrenheit ou Celcius ? 1/2 :")

user_temp = int(input("Rentrez une température :"))

if user_choice == "1":
    final = (user_temp - 32) * (5/9)
    unit = "C"
else:
    final = user_temp * ( 9/ 5 ) + 32
    unit = "F"

print(f"La conversion de {user_temp}{"C" if user_choice == "2" else "F"} en {"Fahrenheit" if user_choice == "2" else "Celcius"} est {final}{unit}.")