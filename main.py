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
exit_option = {
    "1": 1,
    "y": 1,
    "yes": 1,
    "2": 2,
    "n": 2,
    "no": 2
}
events = {
    "negative": [
        {
            "name": "Hardware Malfunction", 
            "server_capacity": -15, "user_amount": 0
        },
        {
            "name": "DDoS Attack", 
            "server_capacity": 0, "user_amount": 30
        },
        {
            "name": "Database Corruption", 
            "server_capacity": -10, "user_amount": -5
        },
        {
            "name": "Critical Rack Failure", 
            "server_capacity": -25, "user_amount": 0
        },
        {
            "name": "Massive User Migration", 
            "server_capacity": 0, "user_amount": 25
        },
        {
            "name": "Security Breach", 
            "server_capacity": -10, "user_amount": -15
        },
        {
            "name": "Heavy Latency Spike", 
            "server_capacity": 0, "user_amount": 10
        }
    ],
    "neutral_positive": [
        {
            "name": "Infrastructure Upgrade", 
            "server_capacity": 20, "user_amount": 0
        },
        {
            "name": "Viral Marketing", 
            "server_capacity": 15, "user_amount": 25
        },
        {
            "name": "Cloud Integration", 
            "server_capacity": 25, "user_amount": 5
        },
        {
            "name": "New Tech Partnership", 
            "server_capacity": 20, "user_amount": 10
        },
        {
            "name": "Node Optimization", 
            "server_capacity": 10, "user_amount": 0
        },
        {
            "name": "Stable Growth", 
            "server_capacity": 10, "user_amount": 5
        }
    ]
}
dias_semana = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def dia_semana(dia):
    dia = dia % 7
    if dia <= 1:
        indice = 0.8
    elif dia >= 5:
        indice = 1.4
    else:
        indice = 1.0
    nombre = dias_semana[dia]
    return dia, indice, nombre
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
def recuento_recursos(energy, cooling_system, server_capacity, user_amount, days_played, nombre, indice, temperature):
    print("\n" + "*"*50)
    print(f"###--- Daily resource manager... (Day {days_played}, {nombre}) ---####\n")
    print(f"--- Energy remaining: {round(energy,2)}")
    print(f"--- Cooling system Integrity: {round(cooling_system,2)}%")    
    print(f"--- Server capacity: {round(server_capacity,0)}")
    print(f"--- System temperature: {round(temperature,2)}°C")
    print(f"--- Users online: {round(user_amount,0)}")
    print(f"--- Events have a {indice}x force\n")
def win_con(days_played, gameplay_exit):
    if days_played == 10:
        gameplay_decision = input("Game won!\nDo you want to keep playing?\n1.Yes\n2.No\n--- ")
        if gameplay_decision in exit_option:
            confirmar_salida = exit_option[gameplay_decision]
            if confirmar_salida == 1:
                print("Starting endless mode...\n")
            elif confirmar_salida == 2:
                print("Thanks for playing!\nClosing...\n")
                gameplay_exit += 1
        else:
            print("Assuming you wanted to keep playing. Starting endless mode...\n")
    return gameplay_exit
def random_event(eventos):
    evento = random.choice(eventos)
    return evento
def probabilidad_dificultad(dificultad):
    if dificultad == 1:
        probabilidad = random.randint(5, 15)
    if dificultad == 2:
        probabilidad = random.randint(20, 40)
    if dificultad == 3:
        probabilidad = random.randint(45, 60)
    return probabilidad
def evento_ocurrido(probabilidad):
    suerte_dia = random.randint(0, 100)
    if suerte_dia < probabilidad:
        evento = random_event(events["negative"])
    else:
        evento = random_event(events["neutral_positive"])
    return evento
def limitadores(energy, cooling_system, server_capacity, user_amount):
    energy = max(0, energy)
    cooling_system = max(0, cooling_system)
    server_capacity = max(0, server_capacity)
    user_amount = max(0, user_amount)
    return energy, cooling_system, server_capacity, user_amount
def recursos_restantes(energy, cooling_system, server_capacity, user_amount, temperature):
    print("###--- Remaining resources...")
    print(f"--- Energy remaining: {round(energy, 1)}")
    print(f"--- Cooling system Integrity: {round(cooling_system, 1)}%")
    print(f"--- Server capacity: {server_capacity}")
    print(f"--- System temperature: {temperature}°C")
    print(f"--- User amount: {user_amount}")
def recursos_afectados(evento,indice):
    print(f"!!!--- Event happened: {evento['name']}\n")
    print("###--- Resources affected...")
    print(f"--- Server capacity: {evento['server_capacity']*indice}")
    print(f"--- Users online: {evento['user_amount']*indice}\n")
def cambio_recursos(energy, cooling_system, server_capacity, user_amount, evento, indice):
    server_capacity += int(evento['server_capacity']*indice)
    user_amount += int(evento['user_amount']*indice)
    return energy, cooling_system, server_capacity, user_amount
def game_over(energy, temperature, gameplay_exit, user_amount, server_capacity, days_played):
    if energy <= 0:
        print("\n!!!--- Not enough energy to mantain the system online, shuting down...")
        print(f"###--- GAME OVER (lasted {days_played} days)")
        gameplay_exit += 1
    elif temperature >= 80:
        print("\n!!!--- System overheating! shuting down...")
        print(f"###--- GAME OVER (lasted {days_played} days)")
        gameplay_exit += 1
    elif user_amount > server_capacity:
        print("\n!!!--- Server overcrowding! shuting down...")
        print(f"###--- GAME OVER (lasted {days_played} days)")
        gameplay_exit += 1
    return gameplay_exit
def cambio_temperatura(cooling_system, temperature, difficulty):
    if difficulty == 1:
        if cooling_system < 60:
            temperature += (60-cooling_system)/5
        elif cooling_system >= 60:
            temperature -= 2
    elif difficulty == 2:
        if cooling_system < 70:
            temperature += (70-cooling_system)/4
        elif cooling_system >= 70:
            temperature -= 2            
    elif difficulty == 3:
        if cooling_system < 80:
            temperature += (80-cooling_system)/3
        elif cooling_system >= 80:
            temperature -= 2            
    temperature += 2
    return round(temperature, 2)
def consumo_recursos(energy, cooling_system, user_amount, difficulty):
    if difficulty == 1:
        energy -= user_amount/10
        cooling_system -= user_amount/10
        print(f"###--- The system consumed resources this day!")
        print(f"--- Energy consumed: -{user_amount/10}")
        print(f"--- Cooling system integrity consumed: -{user_amount/10}%\n")
    elif difficulty == 2:
        energy -= user_amount/8
        cooling_system -= user_amount/8
        print(f"###--- The system consumed resources this day!")
        print(f"--- Energy consumed: -{user_amount/8}")
        print(f"--- Cooling system integrity consumed: -{user_amount/8}%\n")
    elif difficulty == 3:
        energy -= user_amount/5
        cooling_system -= user_amount/5
        print(f"###--- The system consumed resources this day!")
        print(f"--- Energy consumed: -{user_amount/5}")
        print(f"--- Cooling system integrity consumed: -{user_amount/5}%\n")
    return energy, cooling_system
def incremento_diario_clientes(user_amount):
    incremento = random.randint(0,10)
    print(f"###--- The user amount increased by {incremento}!!\n")
    user_amount += incremento
    return user_amount
print("\n" + "*"*50)
print("###--- Welcome to Data Center Control! ---###")
print("*"*50)
player_name = ""
while not player_name.strip(): 
    player_name = input("\n###--- Please enter your name:\n--- ")
    if not player_name.strip():
        print("\n!!!--- No puedes dejar este campo vacio.")
salir = 0 
while salir == 0:
    user_option = input("\n###--- Please select an option below:\n1.New game\n2.Salir\n--- ").lower().strip()
    if user_option in opciones_menu:
        option = opciones_menu[user_option]
        if option == 1:
            print("\n###--- Iniciando partida...\n")

            difficulty = None
            while difficulty == None:
                difficulty_option = input("\n###--- Please choose a difficulty:\n1.Easy\n2.Medium\n3.Hard\n--- ")
                if difficulty_option in opciones_dificultad:
                    difficulty = opciones_dificultad[difficulty_option]
                    difficulty_name = {
                        1: "easy",
                        2: "medium",
                        3: "hard"
                    }
                    print("\n" + "*"*50)
                    print(f"###--- Welcome back, Admin {player_name.capitalize()}. ---###")
                    print(f"###--- Difficulty selected: {difficulty_name[difficulty].upper()} ---###")
                    print("*"*50 + "\n")

                    energy, cooling_system, server_capacity, user_amount = asignador_recursos(difficulty)
                    days_played = 0
                    gameplay_exit = 0
                    dia = random.randint(0, 6)
                    probabilidad = probabilidad_dificultad(difficulty)
                    temperature = 35
                    while gameplay_exit == 0:

                        days_played += 1

                        if days_played > 10:
                            probabilidad = min(100, probabilidad + 1)

                        dia, indice, nombre = dia_semana(dia)

                        recuento_recursos(energy, cooling_system, server_capacity, user_amount, days_played, nombre, indice, temperature)

                        if days_played > 1:
                            energy, cooling_system = consumo_recursos(energy, cooling_system, user_amount, difficulty)
                            temperature = cambio_temperatura(cooling_system, temperature, difficulty)
                            user_amount = incremento_diario_clientes(user_amount)

                        evento = evento_ocurrido(probabilidad)

                        energy, cooling_system, server_capacity, user_amount = cambio_recursos(energy, cooling_system, server_capacity, user_amount, evento, indice)

                        energy, cooling_system, server_capacity, user_amount = limitadores(energy, cooling_system, server_capacity, user_amount)

                        recursos_afectados(evento, indice)

                        recursos_restantes(energy, cooling_system, server_capacity, user_amount, temperature)
                         
                        gameplay_exit = game_over(energy, temperature, gameplay_exit, user_amount, server_capacity, days_played)
                        if gameplay_exit > 0:
                            break
                        
                        gameplay_exit = win_con(days_played, gameplay_exit)
                        if gameplay_exit > 0:
                            break



                        salto = input("\nNext day... (Press ENTER)")

                        dia += 1
                else:
                    print("\nPlease enter a valid option...")

        elif option == 2:
            print("Thanks for playing!\nClosing...\n")
            salir += 1
        else:
            print("Thats not a valid option...\n")
    else:
        print("\nPlease enter a valid option...")
