import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL,
        salario REAL,
        nome_escola TEXT
    )
    """)
    conexao.commit()

nome_professor = input("NOME: ")




while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno") 
        print("2. Listar Alunos") 
        print("3. Atualizar Aluno") 
        print("4. Excluir Aluno") 
        print("5. Sair")
        opcao = input("Escolha uma opção: ") 

    while opcao != 5:
        if opcao == '1': cadastrar() 
        elif opcao == '2': listar()
        elif opcao == '3': atualizar() 
        elif opcao == '4': excluir() 
        elif opcao == '5': break 
        else: print("Opção inválida!")
menu()