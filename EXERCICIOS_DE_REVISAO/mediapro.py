n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

notas = [n1, n2, n3, n4]

soma = 0
for n in notas:
    soma = soma + n


media = soma / 4
print(f"Média: {media}")

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")