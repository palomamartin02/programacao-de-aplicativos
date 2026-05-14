def criar_arquivo():
    open('habitos.txt.', 'w'). close()


def criar():
    habito = (input("NOVO HÁBITO QUE DESEJA ADOTAR: "))
    with open('habitos.txt', 'a') as f:
        f.write(habito + '\n')
    print("Novo hábito adicionado à lista!")

def ler():
    with open('habitos.txt', 'r') as f:
        habitos = f.readlines()

        i = 0
        for h in habitos:
            print(f"{i} - {h.strip()}") 
            i += 1


def atualizar():
    ler()
    idx = int(input("Digite o ID do hábito que deseja alterar: "))
    novo_nome = input("Novo hábito: ")

    with open('habitos.txt', 'r') as f:
        linhas = f.readlines()

    linhas[idx] = novo_nome + '\n'

    with open('habitos.txt', 'w') as f:
        f.writelines(linhas)
    print("Hábito Atualizado!")


def deletar():
    ler()
    idx = int(input("Digite o ID do hábito que deseja excluir: "))
    
    with open('habitos.txt', 'r') as f:
        linhas = f.readlines()
    
    del linhas[idx] 
    
    with open('habitos.txt', 'w') as f:
        f.writelines(linhas)
    print("Hábito Removido!")


while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': 
        criar()
    elif opcao == '2': 
        ler()
    elif opcao == '3': 
        atualizar()
    elif opcao == '4': 
        deletar()
    elif opcao == '5': 
        print("Encerrando Programa...")
        break
