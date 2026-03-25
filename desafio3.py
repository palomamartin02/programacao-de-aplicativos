livros_disponiveis = ["python pro", "banco de dados", "redes", "ia", "hardware"]
livros_emprestados = []

# Operação de Empréstimo
nome_livro = input("Digite o nome do livro que deseja: ")
if nome_livro in livros_disponiveis:
    livros_emprestados.append(nome_livro)
    livros_disponiveis.remove(nome_livro)
    print("Empréstimo realizado com sucesso!")

else:
    print("Desculpe, este livro não está no acervo.")

# Operação de Devolução    
nome2 = input("Digite o nome do livro que está devolvendo: ")
if nome2 in livros_emprestados:
    livros_disponiveis.append(nome2)
    livros_emprestados.remove(nome2)

else:
    print("Este livro não consta como emprestado.")

# Manutenção do Acervo
del livros_disponiveis[0:2]

# Relatório Final
print(f"Estado final das listas: livros_disponiveis {livros_disponiveis}")
print(f"livros_emprestados{livros_emprestados}.")