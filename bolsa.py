media = float (input("digite a sua média: "))
renda_familiar = float (input("digite sua renda: "))
veio_de_escola_publica = input("veio de escola pública? (S/N: ")

if  (media >= 8.0 and renda_familiar < 2.000) or veio_de_escola_publica == "S":
    print("Ganhou a bolsa!")

elif (media < 8.0 and renda_familiar >= 2.000) or veio_de_escola_publica == "N":
    print("Não atende aos requisitos!")
