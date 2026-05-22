import json # Inclui o módulo json integrado no seu script.
import os # Importa a biblioteca json, usada para salvar e ler dados no formato JSON.

BANCO_DADOS = 'alunos.json' #Cria uma variável com o nome do arquivo onde os alunos serão salvos.

def cadastrar(): # Cria uma função chamada cadastrar.
    print("\n--- Novo Cadastro ---") # Mostra "--- Novo Cadastro ---" no terminal e o"\n" pula uma linha.
    
    if os.path.exists(BANCO_DADOS): # Verifica se o Arquivo existe.
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Abre o arquivo em modo leitura 'r'. "encoding='utf-8" representa quase todos os caracteres e permite usar acentos.
            alunos = json.load(f) # Lê dados JSON do arquivo e os converte em um objeto Python.
    else:
        alunos = [] # Se o arquivo não existir, crie uma lista vazia.

    novo_aluno = { #Cria um dicionário.
        "nome": input("Nome: "), # Pede o nome.
        "telefone": input("Telefone: "), # Pede o telefone.
        "turma": input("Turma: "), # Pede a turma.
        "idade": int(input("Idade: ")), # Pede a cidade.
        "cpf": input("CPF: ") #pede o CPF.
    }
    
    alunos.append(novo_aluno) # Adiciona o novo aluno e os dados na lista "alunos".

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # Abre o arquivo em modo escrita "w".
        json.dump(alunos, f, indent=4, ensure_ascii=False) # Salva os dados no json.
        
    print("Aluno cadastrado com sucesso!") # Mostra a mensagem "Aluno cadastrado com sucesso!" no terminal.

def listar(): #Cria uma função chamada listar.
    print("\n--- Lista de Alunos ---") #  Mostra "--- Lista de Alunos ---" no terminal e o"\n" pula uma linha.
    
    if os.path.exists(BANCO_DADOS): # Verifica se o Arquivo existe.
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Abre o arquivo em modo de leitura "r" e "encoding='utf-8" representa quase todos os caracteres e permite usar acentos.
            alunos = json.load(f) # Lê dados JSON do arquivo e os converte em um objeto Python.
    else:
        alunos = []  # Se o arquivo não existir, crie uma lista vazia.

    if not alunos: # Verifica se a lista está vazia.
        print("Nenhum aluno cadastrado.") # Mostra "Nenhum aluno cadastrado."
        return # Encerra função.

    for aluno in alunos: # Percorre todos os alunos.
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # Mostra os dados do aluno.

def atualizar(): # Cria uma função para atualizar aluno.
    print("\n--- Atualizar Aluno ---") # Mostra "--- Atualizar Aluno ---" no terminal e o"\n" pula uma linha.
    if not os.path.exists(BANCO_DADOS): # Se o arquivo nao existir:.
        print("Nenhum aluno cadastrado no sistema.") # Mostra "Nenhum aluno cadastrado no sistema."
        return # Encerra função.

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Abre o arquivo em modo de leitura "r" e "encoding='utf-8" representa quase todos os caracteres e permite usar acentos.
        alunos = json.load(f) # Lê dados JSON do arquivo e os converte em um objeto Python.
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # Pede CPF.
    
    for aluno in alunos: # Percorre todos os alunos.
        if aluno['cpf'] == cpf_busca: # Verifica se encontrou o CPF.
            print(f"Editando dados de: {aluno['nome']}") # Mostra "Editando dados de: {aluno['nome']}" no terminal.
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # Atualiza nome.
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']  # Atualiza telefone.
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']  # Atualiza turma.
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])  # Atualiza idade.
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']  # Atualiza CPF.
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # Abre o arquivo em modo escrita "w" e "encoding='utf-8" representa quase todos os caracteres e permite usar acentos.
                json.dump(alunos, f, indent=4, ensure_ascii=False) # Salva os dados no json.
            print("Dados atualizados com sucesso!") # Mostra "Dados atualizados com sucesso!" no terminal.
            return # Encerra função.

            
    print("Aluno não encontrado.") # Mostra "Aluno não encontrado." no terminal.

def excluir(): # Cria uma função pra excluir.
    print("\n--- Excluir Aluno ---") # Mostra "--- Excluir Aluno ---" e o "\n" pula uma linha.
    if not os.path.exists(BANCO_DADOS): # Se o arquivo não existir:.
        print("Nenhum aluno cadastrado no sistema.") # Mostra "Nenhum aluno cadastrado no sistema." no terminal.
        return # Encerra função.


    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  # Abre o arquivo em modo leitura "r" e "encoding='utf-8" representa quase todos os caracteres e permite usar acentos.
            json.dump([], f) # Cria arquivo vazio.
        alunos = json.load(f) # Lê dados JSON do arquivo e os converte em um objeto Python.
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) # Pede ID.
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # Cria nova lista sem o aluno escolhido.
    
    if len(nova_lista) < len(alunos): # Compara as listas.
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # Abre o arquivo em modo escrita "w" e "encoding='utf-8" representa quase todos os caracteres e permite usar acentos.
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # Salva a nova lista no arquivo JSON.
        print("Aluno removido com sucesso!") # Mostra "Aluno removido com sucesso!" no terminal.
    else: # Se a lista não diminuir.
        print("Aluno não encontrado.") # Mostra "Aluno não encontrado." no terminal.

def menu(): # Cria um menu.
    if not os.path.exists(BANCO_DADOS): # Se o arquivo não existir:.
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # Abre o arquivo em modo escrita "w" e "encoding='utf-8" representa quase todos os caracteres e permite usar acentos.
            json.dump([], f) # Cria arquivo vazio.

    while True:
        print("\n=== SISTEMA ESCOLAR ===") # Mostra mensagem.
        print("1. Cadastrar Aluno") # Mostra mensagem.
        print("2. Listar Alunos") # Mostra mensagem.
        print("3. Atualizar Aluno") # Mostra mensagem.
        print("4. Excluir Aluno") # Mostra mensagem.
        print("5. Sair") # Mostra mensagem.
        
        opcao = input("Escolha uma opção: ") # Pede para escolher uma opção.
        
        if opcao == '1': cadastrar() # Se a opção for 1, cadastra um novo aluno.
        elif opcao == '2': listar() # Se a opção for 2, mostra a lista de alunos cadastrados.
        elif opcao == '3': atualizar() # Se a opção for 3, atualiza um aluno.
        elif opcao == '4': excluir() # Se a opção for 4, exclui um aluno.
        elif opcao == '5': break # Se a opção for 5, encerra o programa.
        else: print("Opção inválida!") # Se não for nenhuma das opções acima, mostra "Opção inválida!" no terminal.

menu() # Executa o programa.