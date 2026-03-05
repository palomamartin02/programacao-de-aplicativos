temperatura = float(input("digite a temperatura: "))

if temperatura <= 30:
    print("Clima estável.")

elif temperatura > 30:
    print("Alerta de Calor!")

    umidade = float(input("digite a umidade:(%) "))

    if umidade < 40:
        print("Ação: Ligar irrigação!")

    else:
        print("Ação: Ligar apenas ventiladores.")