import random # En esta línea se importa 
# el módulo random, que posteriormente será 
# utilizado para generar números aleatorios, 
# seleccionar eventos al azar y calcular 
# probabilidades dentro del juego.
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
events = { # events es un diccionario que contiene 
# dos claves: negative y neutral_positive. Cada una 
# de estas claves almacena una lista de eventos. Cada 
# evento dentro de la lista es un diccionario que 
# contiene tres pares clave-valor: el nombre del evento 
# (name), el cambio en la capacidad del servidor 
# (server_capacity) y el cambio en la cantidad de usuarios 
# (user_amount).
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
dias_semana = { # Python indexa listas desde 0
#Entonces usar 0-6 hace que sea más natural y practico
# trabajar scon cálculos.
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

# En esta sección del programa se definen varias 
# estructuras de datos llamadas diccionarios. Estos 
# diccionarios almacenan opciones del menú, niveles 
# de dificultad, respuestas de salida y los eventos 
# que pueden ocurrir en el juego. También se define 
# un diccionario que relaciona números con los días 
# de la semana. Estas estructuras permiten que el 
# programa interprete entradas del usuario y gestione 
# eventos aleatorios dentro del simulador del centro de 
# datos.

def dia_semana(dia):
    dia = dia % 7 #El operador % es módulo.
    if dia <= 1: # Determinar índice de impacto del evento
        indice = 0.8
    elif dia >= 5:
        indice = 1.4
    else:
        indice = 1.0
    nombre = dias_semana[dia]
    return dia, indice, nombre # retorna tres valores:
# numero del dia, indice del evento & nombre del dia

def asignador_recursos(difficulty): # Inicializa los recursos del juego cuando empieza la partida
    # 100% de capacidad inicial.
    energy = 100
    cooling_system = 100
    server_capacity = 100
    # Estos valores representan el estado inicial del centro de datos.

    if difficulty == 1: # Los usuarios representan la carga del sistema.
        user_amount = random.randint(4,8) # Usuarios iniciales aleatorios entre...
    elif difficulty == 2:
        user_amount = random.randint(5,10)
    elif difficulty == 3:
        user_amount = random.randint(6,12) # Más usuarios → más consumo → más difícil.
    else:
        print("Please select a valid option...")
    return energy, cooling_system, server_capacity, user_amount

def recuento_recursos(energy, cooling_system, server_capacity, user_amount, days_played, nombre, indice, temperature):
    # Esta función solo imprime el estado actual del sistema; no cambia nada; solo muestra información al jugador.
    print("\n" + "*"*50)
    print(f"###--- Daily resource manager... (Day {days_played}, {nombre}) ---####\n")
    print(f"--- Energy remaining: {round(energy,2)}") # ...,2 significa que le seguira 2 numeros despues de la coma decimal.
    print(f"--- Cooling system Integrity: {round(cooling_system,2)}%")    
    print(f"--- Server capacity: {round(server_capacity,0)}")
    print(f"--- System temperature: {round(temperature,2)}°C")
    print(f"--- Users online: {round(user_amount,0)}")
    print(f"--- Events have a {indice}x force\n") # Events have a {indice} times more force.

def win_con(days_played, gameplay_exit): # verifica si el jugador ganó.
    if days_played == 10: # Si el jugador sobrevive 10 días.
        gameplay_decision = input("Game won!\nDo you want to keep playing?\n1.Yes\n2.No\n--- ")
        if gameplay_decision in exit_option:
            confirmar_salida = exit_option[gameplay_decision]
            if confirmar_salida == 1:
                print("Starting endless mode...\n")
            elif confirmar_salida == 2:
                print("Thanks for playing!\nClosing...\n")
                gameplay_exit += 1 # Esto termina el juego; Porque rompe el while gameplay_exit == 0.
        else:
            print("Assuming you wanted to keep playing. Starting endless mode...\n")  # Esto ocurre si el jugador escribe algo que no está en el diccionario: exit_option
    return gameplay_exit

def random_event(eventos): # Recibe una lista de eventos.
    evento = random.choice(eventos) # Elige uno aleatorio
    return evento # Esto devuelve un diccionario de evento.

def probabilidad_dificultad(dificultad): # Esta función define qué tan probable es un evento negativo.
    if dificultad == 1: # Fácil
        probabilidad = random.randint(5, 15) # %
    if dificultad == 2: # Medio
        probabilidad = random.randint(20, 40) # %
    if dificultad == 3: # Dificil
        probabilidad = random.randint(45, 60) # %
    return probabilidad

def evento_ocurrido(probabilidad): # La función simula la probabilidad de que ocurra un problema en el centro de datos.
    suerte_dia = random.randint(0, 100)
    if suerte_dia < probabilidad:
        evento = random_event(events["negative"])
    else:
        evento = random_event(events["neutral_positive"])
    return evento

def limitadores(energy, cooling_system, server_capacity, user_amount): # Evita valores negativos.
    energy = max(0, energy) # max() devuelve el número más grande entre los argumentos. Energy nunca puede ser negativa; si energy = -5, se convierte en energy = 0
    cooling_system = max(0, cooling_system) # max(0, 50) = 50; 
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

    # La función recursos_restantes() no modifica ningún valor del juego.
    # Su función es mostrar en pantalla el estado actual de los recursos 
    # del sistema después de que se hayan aplicado los eventos, el 
    # consumo diario y los cambios de temperatura.
    # Para mejorar la presentación de los datos, utiliza la función 
    # round() para redondear los valores decimales a un solo decimal.

def recursos_afectados(evento,indice): # Muestra el evento ocurrido.
    print(f"!!!--- Event happened: {evento['name']}\n")
    print("###--- Resources affected...")
    print(f"--- Server capacity: {evento['server_capacity']*indice}") # El indice sirve para multiplicar el   
    print(f"--- Users online: {evento['user_amount']*indice}\n") # valor inicializado dependiendo de la dificultad (1.4 o 0.8)

def cambio_recursos(energy, cooling_system, server_capacity, user_amount, evento, indice): # Aplica el cambio al sistema.
    server_capacity += int(evento['server_capacity']*indice)
    user_amount += int(evento['user_amount']*indice)
    return energy, cooling_system, server_capacity, user_amount
    # cambio_recursos() es el complemento de def recursos_afectados():

def game_over(energy, temperature, gameplay_exit, user_amount, server_capacity, days_played): # Verifica condiciones de derrota.
    if energy <= 0:
        print("\n!!!--- Not enough energy to mantain the system online, shuting down...")
        print(f"###--- GAME OVER (lasted {days_played})")
        gameplay_exit += 1 # Esto termina el juego; Porque rompe el while gameplay_exit == 0.
    elif temperature >= 80:
        print("\n!!!--- System overheating! shuting down...")
        print(f"###--- GAME OVER (lasted {days_played})")
        gameplay_exit += 1 # Esto termina el juego; Porque rompe el while gameplay_exit == 0.
    elif user_amount > server_capacity: 
        print("\n!!!--- Server overcrowding! shuting down...")
        print(f"###--- GAME OVER (lasted {days_played})")
        gameplay_exit += 1 # Esto termina el juego; Porque rompe el while gameplay_exit == 0.
    return gameplay_exit

def cambio_temperatura(cooling_system, temperature, difficulty): # Simula calentamiento del sistema.
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

def consumo_recursos(energy, cooling_system, user_amount, difficulty): # Simula consumo diario del sistema.
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

def incremento_diario_clientes(user_amount): # Cada día los usuarios aumentan.
    incremento = random.randint(0,10)
    print(f"###--- The user amount increased by {incremento}!!\n")
    user_amount += incremento
    return user_amount

print("\n" + "*"*50)
print("###--- Welcome to Data Center Control! ---###")
print("*"*50)
player_name = ""

while not player_name.strip(): # Este while obliga al jugador a escribir un nombre válido.
    player_name = input("\n###--- Please enter your name:\n--- ")
    if not player_name.strip(): # strip() elimina espacios al inicio y final.
        print("\n!!!--- No puedes dejar este campo vacio.")
# Mientras este vacio el campo player_name esta condicion de bucle es TRUE 
# y se repetira el bucle hasta que se inserte un nombre  se cancele la condicion del bucle.

salir = 0 # Esta variable controla si el programa termina o sigue en el menú. Cuando salir cambia a 1, el juego termina.

while salir == 0: # Mientras salir sea 0, el menú seguirá apareciendo. 
    user_option = input("\n###--- Please select an option below:\n1.New game\n2.Salir\n--- ").lower().strip() # Esto evita errores de escritura del jugador.
    if user_option in opciones_menu: # Del diccionario opciones_menu
        option = opciones_menu[user_option]
        if option == 1: # empieza el juego!!
            print("\n###--- Iniciando partida...\n")

            difficulty = None
            while difficulty == None: # Esto repite la pregunta hasta que el jugador elija una dificultad válida.
                difficulty_option = input("\n###--- Please choose a difficulty:\n1.Easy\n2.Medium\n3.Hard\n--- ")
                if difficulty_option in opciones_dificultad: # Del diccionario opciones_dificultad
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

                    energy, cooling_system, server_capacity, user_amount = asignador_recursos(difficulty) # Esta función crea los valores iniciales del juego.
                    # Variables de control
                    days_played = 0 # días sobrevividos
                    gameplay_exit = 0 # controla si termina
                    dia = random.randint(0, 6) # día de la semana random
                    probabilidad = probabilidad_dificultad(difficulty) # probabilidad de evento
                    temperature = 35 # temperatura inicial
                    while gameplay_exit == 0: # Bucle principal

                        days_played += 1

                        if days_played > 10: # Después del día 10 → los eventos se vuelven más probables.
                            probabilidad = min(100, probabilidad + 1)  # Evita que supere 100%

                        dia, indice, nombre = dia_semana(dia) #  la función devuelve: ejemplo: 3 , 2 , "Wednesday"

                        recuento_recursos(energy, cooling_system, server_capacity, user_amount, days_played, nombre, indice, temperature) # Muestra en pantalla:...

                        if days_played > 1:
                            energy, cooling_system = consumo_recursos(energy, cooling_system, user_amount, difficulty)  # consumo de energía y enfriamiento
                            temperature = cambio_temperatura(cooling_system, temperature, difficulty) # cambio de temperatura
                            user_amount = incremento_diario_clientes(user_amount) # crecimiento de usuarios

                        evento = evento_ocurrido(probabilidad) # Esto decide si ocurre un evento.

                        # Aplicar cambios del evento
                        energy, cooling_system, server_capacity, user_amount = cambio_recursos(energy, cooling_system, server_capacity, user_amount, evento, indice)

                        # Limitar valores
                        energy, cooling_system, server_capacity, user_amount = limitadores(energy, cooling_system, server_capacity, user_amount)

                        # Mostrar evento
                        recursos_afectados(evento, indice)

                        # Mostrar recursos restantes
                        recursos_restantes(energy, cooling_system, server_capacity, user_amount, temperature)
                        
                        # Condición de victoria
                        gameplay_exit = win_con(days_played, gameplay_exit)
                        if gameplay_exit > 0:
                            break
                        
                        # Condición de derrota
                        gameplay_exit = game_over(energy, temperature, gameplay_exit, user_amount, server_capacity, days_played)
                        if gameplay_exit > 0:
                            break

                        # Pasar al siguiente día
                        salto = input("\nNext day... (Press ENTER)") # Esto pausa el juego

                        dia += 1 # Avanzar día de la semana

                else: # Salir del juego
                    print("\nPlease enter a valid option...")

        elif option == 2: # y el while salir == 0 termina.
            print("Thanks for playing!\nClosing...\n")
            salir += 1
        else:
            print("Thats not a valid option...\n")
    else:
        print("\nPlease enter a valid option...")