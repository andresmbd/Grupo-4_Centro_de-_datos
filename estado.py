import random


servidores = 300     # Se degrada
refrigeracion = 10             # Se gasta por ciclo
temperatura = 40               # Tempera inicial

dias_totales = 10
dias = 1

while dias <= dias_totales:

    print(f"\n--- Dias {dias} ---")

    # Generar clientes aleatorios
    clientes = random.randint(0, 500)
    print(f"Clientes: {clientes}")

    if clientes == 0:
        print(" No llegaron clientes. No hay actividad. Simulación detenida.")
        break

    # temperatura
    aumento = random.randint(1, 10)
    temperatura = temperatura + aumento - refrigeracion

    if temperatura < 10:
        temperatura = 10

    print(f"Temperatura actual: {temperatura}°C")

    # Evento crítico: Servidores quemados
    if temperatura > 80:
        print("¡ALERTA! La temperatura superó 80°C. Los servidores se quemaron.")
        break

    # 3. Revisar sobrecarga por clientes
    if clientes > servidores:
        perdida = clientes - servidores
        print(f"Sobrecarga. Se pierden {perdida} clientes.")
    else:
        print("Capacidad suficiente para todos los clientes.")

   
    # servidores se degrada
    servidores -= 1
    print(f"Capacidad de servidores restante: {servidores}")

    if servidores <= 0:
        print("No quedan servidores operativos. Simulación detenida.")
        break

    # Refrigeración se consume
    refrigeracion -= 1
    print(f"Refrigeración restante: {refrigeracion}")

    if refrigeracion <= 0:
        print(" La refrigeración llegó a 0. La temperatura ya no puede ser controlada.")
        break

    salto = input ("pasar al siguiente dia ")
    dias += 1
