def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def get_temperature_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

user_choice = 0

while user_choice not in ["1", "2"]:
    user_choice = input("Convertir en Fahrenheit ou Celcius ? 1/2 : ")

user_temp = get_temperature_input("Rentrez une température : ")

if user_choice == "1":
    final = convert_to_celsius(user_temp)
    unit = "C"
else:
    final = convert_to_fahrenheit(user_temp)
    unit = "F"

print(f"La conversion de {user_temp}{'C' if user_choice == '1' else 'F'} en {'Fahrenheit' if user_choice == '2' else 'Celcius'} est {final:.2f}{unit}.")
