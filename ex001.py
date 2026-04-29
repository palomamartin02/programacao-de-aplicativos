def converter_km_para_ms(velocidade_km):
    velocidade_ms = velocidade_km / 3.6
    return velocidade_ms

velocidade = float(input("Velocidade atual (km/h)?: "))
if velocidade > 80:
    v_ms = converter_km_para_ms(velocidade)
    print(f"Velocidade em m/s: {v_ms} m/s.")
    print("Reduza a velocidade!")