codigo = int(input("Digite o código do pacote: "))
peso = int(input("Digite o peso: "))

if peso > 50:
    print("Carga Pesada!")

#ENTREGA EXPRESSA
if peso < 5 and codigo % 10 == 0:
    print(f"Pacote {codigo}: entrega expressa")
