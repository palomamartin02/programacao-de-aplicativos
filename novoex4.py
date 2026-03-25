cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nome = input("Digite o nome de uma cidade: ")

if nome in cidades:
    indice = cidades.index(nome)
    print(f"A cidade {nome} esta na posição {indice}")

else:
     print("Cidade não encontrada.")