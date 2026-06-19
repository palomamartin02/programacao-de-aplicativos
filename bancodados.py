import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

def cadastrar_aluno():
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

    print(f"Passo 3: Dados da {nome_aluno} gravados com sucesso!")

# LISTAR

def listar_alunos():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    print("\n LISTA DE ALUNOS:  ")
    for aluno in alunos:
        print(alunos)




def buscar_alunos():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual seu ID: "))

    cursor.execute(f'''SELECT nome , cpf , telefone , idade , turma FROM alunos WHERE id = {id_aluno}''')
        
    aluno = cursor.fetchone()

    if not aluno:
            print(" Não encontrado ")
    else:
            print(f" Nome atual {aluno[0]} ")
            print(f" CPF atual {aluno [1]} ")
            print(f" Telefone atual {aluno[2]} ")
            print(f" Idade atual {aluno [3]} ")
            print(f" Turma atual {aluno [4]} ")

            nome_atualizado = input(" Atualize seu nome: ")
            cpf_atualizado = input(" Atualize seu CPF: ")
            telefone_atualizado = input(" Atualize se telefone: ")
            idade_atualizada = input(" Atualize sua idade: ")
            turma_atualizada = input(" Atualize sua turma: ")

            cursor.execute(f'''
                            UPDATE alunos
                            SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}', Telefone ='{telefone_atualizado}', Idade ='{idade_atualizada}', Turma ='{turma_atualizada}'
                        WHERE id ={id_aluno}
                            ''')
            conexao.commit()
            print(" Dados alterados ")



def deletar():

    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual ID deseja deletar: " ))

        # Verifica se o aluno existe
    cursor.execute(f'''SELECT id FROM Alunos WHERE Id = {id_aluno}''')
    aluno = cursor.fetchone()

    if not aluno:
        print ("Aluno não encontrado ")
    else:
        cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
        conexao.commit()
        print("aluno deletado")



BANCO_DADOS = 'escola_demonstracao.db'

def cadastrar_professor():
    print("\n--- Novo Cadastro ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    materia = input("Materia: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salário: "))
    escola = input("Escola: ")

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    comando = f'''
        INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, escola)
        VALUES ('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', {salario}, '{escola}')
    '''
    cursor.execute(comando)
    conexao.commit()
    print("Professor cadastrado com sucesso!")

def listar_professores():
    print("\n--- Lista de professores ---")
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()


    cursor.execute("SELECT * FROM professores")
    todos_professores = cursor.fetchall()

    if not todos_professores:
        print("Nenhum Professor cadastrado.")
    else:
        for p in todos_professores:
            print(f"ID: {p[0]} | Nome: {p[1]} | Matéria: {p[3]} | CPF: {p[5]}")


def atualizar_professor():
    print("\n--- Atualizar Dados ---")
    id_busca = int(input("Digite o ID do Professor que deseja editar: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()


    cursor.execute(f"SELECT * FROM professores WHERE id = {id_busca}")
    professor = cursor.fetchone() 

    if not professor:
        print("Professor não encontrado.")
        return

    print(f"Editando dados de: {professor[1]}")
    novo_nome = input(f"Novo Nome ({professor[1]}): ")
    novo_tel = input(f"Novo Telefone ({professor[2]}): ")
    nova_materia = input(f"Nova Matéria ({professor[3]}): ")
    nova_idade = int(input(f"Nova Idade ({professor[4]}): "))
    novo_cpf = input(f"Novo CPF ({professor[5]}): ")
    novo_salario = float(input(f"Novo Salário ({professor[6]}): "))
    nova_escola = input(f"Nova Escola ({professor[7]}): ")

    comando = f'''
        UPDATE professores 
        SET nome = '{novo_nome}', telefone = '{novo_tel}', turma = '{nova_materia}', 
                    idade = {nova_idade}, cpf = '{novo_cpf}',
                    salario = {novo_salario}, escola = '{nova_escola}'
        WHERE id = {id_busca}
    '''

    cursor.execute(comando)
    conexao.commit()
    print("Dados atualizados com sucesso!")

def excluir_professor():
    print("\n--- Excluir Professor ---")
    id_busca = int(input("Digite o ID do Professor que deseja remover: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    comando = f"DELETE FROM professores WHERE id = {id_busca}"
    
    cursor.execute(comando)
    conexao.commit()

   


def menu():
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            materia TEXT,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            salario REAL,
            escola TEXT
        )
    ''')

    conexao.commit()
    

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Atualizar Professor")
        print("4. Excluir Professor")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()
conexao.close()
