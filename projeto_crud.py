estoque = []

# Adiciona um novo item à lista
def adicionar_produto(nome):
    estoque.append(nome)

# Percorre a lista e exibe os itens com seus respectivos índices
def listar_produtos(produtos):
    i = 0
    for produto in produtos:
        indice = produtos.index(produto)
        print(f"{indice} - {produto}")

# Substitui o nome de um produto existente pelo novo nome informado
def atualizar_produto(indice, novo_nome):
    produtos[indice] = novo_nome


#  Remove o item da lista utilizando a posição (índice)
def remover_produto(indice):
    produtos.pop(indice)


def exibir_menu(opcao):
    while True:
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            adicionar_produto(nome)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            indice = int(input("Índice: "))
            novo_nome = input("Novo nome: ")
            atualizar_produto(indice, novo_nome)

        elif opcao == "4":
            indice = int(input("Índice: "))
            remover_produto(indice)

        elif opcao == "5":
            break

opcao = ""
exibir_menu(opcao)