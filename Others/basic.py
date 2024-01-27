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

def main():
    user_choice = input("Convertir en Fahrenheit ou Celsius ? (1/2) : ")

    if user_choice not in ["1", "2"]:
        print("Choix invalide. Veuillez entrer '1' pour Fahrenheit ou '2' pour Celsius.")
        return

    user_temp = get_temperature_input("Rentrez une température : ")

    if user_choice == "1":
        converted_temp = convert_to_celsius(user_temp)
        from_unit, to_unit = "Fahrenheit", "Celsius"
    else:
        converted_temp = convert_to_fahrenheit(user_temp)
        from_unit, to_unit = "Celsius", "Fahrenheit"

    print(f"La conversion de {user_temp}°{from_unit} en {to_unit} est {converted_temp:.2f}°{to_unit}.")

if __name__ == "__main__":
    main()
