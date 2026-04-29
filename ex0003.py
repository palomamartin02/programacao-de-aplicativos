n = input("Nome: ")
p = float(input("Peso: "))
a = float(input("Altura: "))
i = int(input("Idade: "))

def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = peso / (altura **2)

    if imc < 18.5:
        resultado = "Baixo Peso"

    elif imc < 25:
        resultado = "Normal"

    elif imc < 30:
        resultado = "Sobrepeso"    

    else:
        resultado = "Obesidade"

   
    return f"{nome}, {idade} anos: IMC {imc} - {resultado}"

print(gerar_relatorio_saude(n, p, a, i))    