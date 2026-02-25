temperatura = float(input("digite a temperatura do servidor"))

if temperatura >= 80:
    print ("PERIGO! Desligando servidor por superaquecimento!")
elif temperatura >= 50 < 80: 
    print ("Alerta: ventoinhas ligadas no máximo!")
elif temperatura < 50:
    print ("Temperatura estável. Sistema operando normalmente")
