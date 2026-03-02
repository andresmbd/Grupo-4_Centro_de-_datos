# SELECTOR DE DIFICULTAD

dificultades = {
    "1": "facil",
    "facil": "facil",
    "2": "medio",
    "medio": "medio",
    "3": "dificil",
    "dificil": "dificil",
    "d": "dificil",
    "m": "medio",
    "f": "facil"
}

try:
    print("*"*50)
    print("Dificultades: \n1. Easy\n2. Medium\n3. Hard")
    dificultad = input("Por favor selecciona la dificultad del juego: ").lower()
    
except ValueError:
    print("Ha ocurrido un error de valor.")

