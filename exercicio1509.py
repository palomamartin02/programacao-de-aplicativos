# EXERCICIO 01
print("---- EXERCÍCIO 01 ----")
def busca_sequencial(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i

    return -1


vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

valor = int(input("Digite um valor: "))

indice = busca_sequencial(vetor, valor)

print("Índice:", indice)
print("\n")




# EXERCICIO 02
print("---- EXERCÍCIO 02 ----")
def contar_valor(vetor, valor):
    contador = 0

    for i in range(len(vetor)):
        if vetor[i] == valor:
            contador += 1

    return contador


vetor = [5, 2, 5, 8, 5, 10, 2, 5, 7, 3]

valor = int(input("Digite o valor: "))

quantidade = contar_valor(vetor, valor)

print("O valor aparece", quantidade, "vezes.")
print("\n")




# EXERCICIO 03
print("---- EXERCÍCIO 03 ----")
vetor = [15, 8, 32, 4, 25, 19, 7, 40, 12, 6]

maior = vetor[0]
posicao = 0

for i in range(1, len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

print("Maior número:", maior)
print("Posição:", posicao)
print("\n")




# EXERCÍCIO 04
print("---- EXERCÍCIO 04 ----")
def buscar_aluno(alunos, nome):
    for i in range(len(alunos)):
        if alunos[i] == nome:
            return True

    return False


alunos = ["Ana", "Carlos", "Joao", "Maria", "Pedro"]

nome = input("Digite o nome do aluno: ")

if buscar_aluno(alunos, nome):
    print("Aluno encontrado.")
else:
    print("Aluno não encontrado.")
print("\n")




# EXERCICIO 05
print("---- EXERCÍCIO 05 ----")
vetor = [5, 2, 8, 5, 10, 5, 7, 3, 5, 9]

valor = int(input("Digite o valor: "))

primeira = -1
ultima = -1

for i in range(len(vetor)):
    if vetor[i] == valor:

        if primeira == -1:
            primeira = i

        ultima = i

print("Primeira posição:", primeira)
print("Última posição:", ultima)
print("\n")





# EXERCICIO 06
print("---- EXERCICIO 06 ----")
def busca_binaria(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == valor:
            return meio

        if valor < vetor[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1


vetor = [2, 5, 8, 12, 15, 20, 25, 30, 35, 40]

valor = int(input("Digite o valor: "))

indice = busca_binaria(vetor, valor)

print("Índice:", indice)
print("\n")





# EXERCICIO 07
print("---- EXERCICIO 07 ----")
def busca_binaria_palavra(palavras, palavra):
    inicio = 0
    fim = len(palavras) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if palavras[meio] == palavra:
            return meio

        if palavra < palavras[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1


palavras = ["Ana", "Carlos", "Joao", "Maria", "Pedro"]

palavra = input("Digite uma palavra: ")

indice = busca_binaria_palavra(palavras, palavra)

if indice != -1:
    print("Palavra encontrada no índice", indice)
else:
    print("Palavra não encontrada.")
print("\n")





# EXERCICIO 08
print("---- EXERCÍCIO 08 ----")
def busca_binaria(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2

        comparacoes += 1

        if vetor[meio] == valor:
            return meio, comparacoes

        if valor < vetor[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1, comparacoes


vetor = [2, 5, 8, 12, 15, 20, 25, 30, 35, 40]

valor = int(input("Digite o valor: "))

indice, comparacoes = busca_binaria(vetor, valor)

print("Índice:", indice)
print("Número de comparações:", comparacoes)
print("\n")





# EXERCICIO 09
print("---- EXERCÍCIO")
def encontrar_posicao(vetor, valor):
    inicio = 0
    fim = len(vetor)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if vetor[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio

    return inicio


vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

valor = int(input("Digite o novo valor: "))

posicao = encontrar_posicao(vetor, valor)

print("O valor deve ser inserido na posição:", posicao)
print("\n")





# EXERCICIO 10
print("---- EXERCÍCIO 10 ----")
vetor = list(range(1, 101))

valores = [10, 50, 90]

for valor in valores:

    # Busca sequencial
    comparacoes_seq = 0

    for i in range(100):
        comparacoes_seq += 1

        if vetor[i] == valor:
            break

    # Busca binária
    inicio = 0
    fim = 99
    comparacoes_bin = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes_bin += 1

        if vetor[meio] == valor:
            break
        elif valor < vetor[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Valor:", valor)
    print("Busca sequencial:", comparacoes_seq, "comparações")
    print("Busca binária:", comparacoes_bin, "comparações")
    print()
print("\n")