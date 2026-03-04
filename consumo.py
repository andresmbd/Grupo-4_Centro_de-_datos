

import random

recursos = {
    "energia": 1000,    
    "servidores_activos": 10,
    "temperatura_actual": 35}

category = random.choice(["negative", "neutral"])
event_ = random.choice([category])

recursos["temperatura_actual"] += event_["temperature"]

recursos["servidores_activos"] -= event_["servers"]

gasto_energia = (recursos["temperatura_actual"] * 2) + (recursos["servidores_activos"] * 5)
recursos["energia"] -= gasto_energia

print(f"  ALERTA: {event_['name']}!")
print(f" Impacto: -{event_['servers']} servidores, +{event_['temperature']}°C")

if recursos["temperatura_actual"] > 60:
    print(" CRÍTICO: ¡Sobrecalentamiento! El sistema se ha apagado por seguridad.")
elif recursos["energia"] <= 0:
    print(" ERROR: Nos hemos quedado sin energía.")
elif recursos["servidores_activos"] <= 0:
    print(" FRACASO: No quedan servidores operativos.")
else:
    print(f" ESTADO: Sistema estable. Energía restante: {recursos['energia']}")