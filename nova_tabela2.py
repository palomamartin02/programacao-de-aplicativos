import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()


def criar_tabela():
    print("\n--- CADASTRO DE PROFESSOR ---")
    nome_professor = input("NOME: ")
    telefone_professor = input("TELEFONE: ")
    materia_professor = input("MATÉRIA: ")
    idade_professor = int(input("IDADE: "))
    cpf_professor = input("CPF: ")
    salario_professor = float(input("SALÁRIO: "))
    nome_da_escola = input("NOME DA ESCOLA: ")

    comando_inserir = f'''
        INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, nome_escola)
        VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', {idade_professor}, '{cpf_professor}', {salario_professor}, '{nome_da_escola}')
    '''
    cursor.execute(comando_inserir)
    conexao.commit()
    print("certo")


def listar():
    cursor = conexao.cursor()

    # MUDANÇA: Substituí o '*' listando coluna por coluna na ordem correta
    cursor.execute("**SELECT id, nome, telefone, materia, idade, cpf, salario, nome_escola FROM professores**")
    professores = cursor.fetchall()

    print("\n LISTA DE PROFESSORES:  ")
    for professor in professores:
        print(f" ID {professor[0]}")
        print(f" Nome {professor[1]} ")
        print(f" Telefone {professor[2]} ")
        print(f" Materia  {professor[3]}")
        print(f" Idade {professor[4]} ")
        print(f" CPF {professor[5]} ")
        print(f" Salario {professor[6]} ")
        print(f" Escola {professor[7]}")
        print("-" * 30)


def atualizar():
    listar()
    cursor = conexao.cursor()

    id_professor = int(input(" Qual seu ID: "))

    # MUDANÇA: Substituí o '*' listando coluna por coluna na busca do ID
    cursor.execute(f'''**SELECT id, nome, telefone, materia, idade, cpf, salario, nome_escola FROM professores** WHERE id = {id_professor}''')
    
    professor = cursor.fetchone()

    if not professor:
        print(" Não encontrado ")
        return
    else:
        print(f" ID atual {professor[0]}")
        print(f" Nome atual {professor[1]} ")
        print(f" Telefone atual {professor[2]} ")
        print(f" Materia atual {professor[3]}")
        print(f" Idade atual {professor[4]} ")
        print(f" CPF atual {professor[5]} ")
        print(f" Salario atual {professor[6]} ")
        print(f" Escola atual {professor[7]}")

    nome_atualizado = input(" Atualize seu nome: ")
    cpf_atualizado = input(" Atualize seu CPF: ")
    telefone_atualizado = input(" Atualize seu telefone: ")
    materia_atualizada = input("Atualize sua matéria: ")
    idade_atualizada = int(input(" Atualize sua idade: "))
    salario_atualizado = float(input(" Atualize seu salário: "))
    nome_escola_atualizado = input("Atualize o nome da escola: ")

    cursor.execute(f'''
                    UPDATE professores
                    SET nome ='{nome_atualizado}', cpf ='{cpf_atualizado}', telefone ='{telefone_atualizado}', idade ={idade_atualizada}, salario ={salario_atualizado}, nome_escola = '{nome_escola_atualizado}', materia = '{materia_atualizada}'
                    WHERE id = {id_professor}
                    ''')
    conexao.commit()
    print(" Dados alterados ")


def deletar():
    cursor = conexao.cursor()

    id_professor = int(input(" Qual ID deseja deletar: " ))

    cursor.execute(f'''SELECT id FROM professores WHERE id = {id_professor}''')
    professor = cursor.fetchone()

    if not professor:
        print ("Professor não encontrado ")
    else:
        cursor.execute(f'''DELETE FROM professores WHERE id = {id_professor}''')
        conexao.commit()
        print("Professor deletado")


def menu():
    cursor.execute('''
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

        if opcao == '1': criar_tabela() 
        elif opcao == '2': listar()
        elif opcao == '3': atualizar() 
        elif opcao == '4': deletar() 
        elif opcao == '5': break
        else:
            conexao.close()
            print("erro")

 
menu()