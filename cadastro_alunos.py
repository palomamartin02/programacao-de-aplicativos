import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

print("Passo 1: Conectado ao banco de dados.")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
''')
print("Passo 2: Tabela e campos configurados.")

nome_aluno = input("NOME: ")
telefone_aluno = input("TELEFONE: ")
turma_aluno = input("TURMA: ")
idade_aluno = int(input("IDADE: "))
cpf_aluno = input("CPF:")

comando_inserir = f'''
    INSERT INTO alunos (nome, telefone, turma, idade, cpf)
    VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno}, '{cpf_aluno}')
'''

cursor.execute(comando_inserir)

conexao.commit()
conexao.close()

print(f"Passo 3: Dados da {nome_aluno} gravados com sucesso!")