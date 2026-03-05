import random
opciones_menu = {
    "1": 1,
    "n": 1,
    "new game": 1,
    "new": 1,
    "game": 1,
    "2": 2,
    "s": 2,
    "salir": 2
}
opciones_dificultad = {
    "1": 1,
    "easy": 1,
    "e": 1,
    "2": 2,
    "medium": 2,
    "m": 2,
    "3": 3,
    "hard": 3,
    "h": 3
}
def asignador_recursos(difficulty):
    energy = 100
    cooling_system = 100
    server_capacity = 100

    if difficulty == 1:
        user_amount = random.randint(4,8)
    elif difficulty == 2:
        user_amount = random.randint(5,10)
    elif difficulty == 3:
        user_amount = random.randint(6,12)
    else:
        print("Please select a valid option...")
    return energy, cooling_system, server_capacity, user_amount

print("*"*50)
print("Welcome to Data Center Control!")
print("*"*50)

player_name = input("Please enter your name: ")
salir = 0 
while salir == 0:
    user_option = input("Please select an option below:\n1.New game\n2.Salir\n--- ").lower().strip()
    if user_option in opciones_menu:
        option = opciones_menu[user_option]
        if option == 1:
            print("Iniciando partida...")

            difficulty = None
            while difficulty == None:
                difficulty_option = input("Please choose a difficulty:\n1.Easy\n2.Medium\n3.Hard\n--- ")
                if difficulty_option in opciones_dificultad:
                    difficulty = opciones_dificultad[difficulty_option]
                    energy, cooling_system, server_capacity, user_amount = asignador_recursos(difficulty)
                    
                else:
                    print("Please enter a valid option...")

        elif option == 2:
            print("Gracias por jugar!\nSaliendo...\n")
            salir += 1
    else:
        print("Por favor selecciona una opcion correcta...\n")
