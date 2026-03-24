autorizados = ["Alice", "Bob", "Carlos"]
nome = input("digite o nome de um pesquisador: ")

# Verificação de Existência
if nome in autorizados:
    indice = autorizados.index(nome)
    print( f"Acesso Permitido! O pesquisador {nome} está na posição {indice}." )

    pergunta = input("Deseja remover esse pesquisador da lista (s/n)?: ")
   
    if pergunta == "s":
        autorizados.remove(nome)
        print(f"Lista atualizada {autorizados}")

    else:
        print("Encerrando Programa!")
else:
    adicionar = input("Deseja cadastrar esse novo pesquisador (s/n)?: ") 
    if adicionar == "s":
        autorizados.append(nome)
        print(f"Lista atualizada{autorizados}")