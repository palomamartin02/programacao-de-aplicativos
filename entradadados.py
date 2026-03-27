compras = []
nome = ""
while nome != "fim":
    nome = input("Digite outro produto: ")
    if nome != "fim":
        compras.append(nome)


for p in compras:
    print(f"{p}")