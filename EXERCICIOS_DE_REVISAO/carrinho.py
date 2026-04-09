lista = []
nome = ""

while nome != "sair":
    nome = input("Digite um nome: ")
    if nome != "sair":
        lista.append(nome)
        print(f"{lista}")