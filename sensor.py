temps = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]

valor = 0
for temperatura in temps:
    if temperatura > 30.0:
        print(f"ALERTA: Temperatura Crítica! ({temperatura}°C)")