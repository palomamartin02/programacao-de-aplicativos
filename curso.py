média = float (input("digite a sua média:"))
presença = int (input ("digite sua porcentagem de presença:"))

if média >= 70 and presença >= 75:
    print ("Parabéns! Você foi aprovado.")

elif média < 70 and presença < 75:
    print("Reprovado. Verifique sua nota ou frequência.")