# --- INTERFAZ DE ESTADO DEL DATA CENTER ---
print("=" * 40)
print(f"|   ESTADO DEL DATA CENTER - DÍA X   |")
print("=" * 40)
print(f"| Temperatura:   {temperatura}°C      |")
print(f"| Servidores:    {servidores} unidades |")
print(f"| Clientes:      {clientes} usuarios  |")
print(f"| Presupuesto:   ${dinero}           |")
print("-" * 40)

# Una pequeña barra visual para la temperatura
if temperatura > 70:
    print("ALERTA: [##########] CRÍTICO")
elif temperatura > 40:
    print("ESTADO: [#####-----] NORMAL")
else:
    print("ESTADO: [##--------] FRÍO")
print("=" * 40)