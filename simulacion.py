import random 

servidores = 300
dias_totales = 10
dias = 1

cerrar = 0
#clientes aleatorios
while cerrar == 0:
    clientes = random.randint(250, 400)
    print(f"\n--- Dias {dias} ---")
    print(f"Clientes en este dia: {clientes}")

    if dias == 10:
        print("Ganaste ")
        opcion = input("Quieres seguir jungando? (s/n) ")
        if opcion == "s":
            print("modo infinito")
        elif opcion == "n":
            print("fin del juego")
            cerrar += 1
        else:
            print("opcion incorrecta")

    if clientes >  servidores:
        perdida = clientes - servidores
        print(f"CAPACIDAD EXCEDIDA {perdida}")
        print("fin del juego")
        cerrar += 1
    elif clientes < servidores:
        print("CAPACIDAD ESTABLE")
        dias += 1 
        salto = input ("pasar al siguiente dia ")

 