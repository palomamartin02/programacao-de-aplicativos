peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso/ altura ** 2
if imc > 25:
    print(f"{imc} SOBREPESO! IMC acima de 25. ")

else:
    print(f"{imc} Peso ideal.")