import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

def criar_tabela():
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

    nome_professor = input("NOME: ")
    telefone_professor =input("TELEFONE: ")
    materia_professor = input("MATÉRIA: ")
    idade_professor = int(input("IDADE: "))
    cpf_professor = input("CPF: ")
    salario_professor = int(input("SALÁRIO: "))
    nome_da_escola = input("NOME DA ESCOLA: ")

    comando_inserir = f'''
        INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, nome_escola)
        VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', {idade_professor}, '{cpf_professor}', '{salario_professor}', '{nome_da_escola}')
    '''
    conexao.commit()
    print("certo")


def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    print("\n LISTA DE PROFESSORES:  ")
    for professor in professores:
        print(f" Nome {professor[0]} ")
        print(f" CPF {professor[1]} ")
        print(f" Materia  {professor[2]}")
        print(f" Telefone {professor[3]} ")
        print(f" Idade {professor[4]} ")
        print(f" Salario {professor[5]} ")
        print(f" Escola {professor[6]}")
        print("-" * 30)
        
       


def atualizar():
     listar()
     conexao = sqlite3.connect('escola_demonstracao.db')
     cursor = conexao.cursor()

     id_professor = int(input(" Qual seu ID: "))

     cursor.execute(f'''SELECT * FROM professores WHERE id = {id_professor}''')
    
     professor = cursor.fetchall()

     if not professor:
        print(" Não encontrado ")
     else:
        print(f" Nome atual {professor[0]} ")
        print(f" CPF atual {professor[1]} ")
        print(f" Materia atual {professor[2]}")
        print(f" Telefone atual {professor[3]} ")
        print(f" Idade atual {professor[4]} ")
        print(f" Salario atual {professor[5]} ")
        print(f" Escola atual {professor[6]}")

        nome_atualizado = input(" Atualize seu nome: ")
        cpf_atualizado = int(input(" Atualize seu CPF: "))
        telefone_atualizado = int(input(" Atualize se telefone: "))
        materia_atualizada = input("Atualize a matéria: ")
        idade_atualizada = int(input(" Atualize sua idade: "))
        salario_atualizado = int(input(" Atualize seu salário: "))
        nome_escola_atualizado = input("Atualize o nome da escola: ")

        cursor.execute(f'''
                        UPDATE professores
                        SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}', Telefone ='{telefone_atualizado}', Idade ='{idade_atualizada}', Salario ='{salario_atualizado}', Escola = '{nome_escola_atualizado}', Materia = '{materia_atualizada}'
                        WHERE id = {id_professor}
                        ''')
        conexao.commit()
        print(" Dados alterados ")




def deletar():
     conexao = sqlite3.connect("escola_demonstracao.db")
     cursor = conexao.cursor()

     id_professor = int(input(" Qual ID deseja deletar: " ))

    # VERIFICA SE O PROFESSOR EXISTE
     cursor.execute(f'''SELECT id FROM professores WHERE id = {id_professor}''')
     professor = cursor.fetchone()

     if not professor:
        print ("Professor não encontrado ")
     else:
        cursor.execute(f'''DELETE FROM professores WHERE Id = {id_professor}''')
        conexao.commit()
        print("Professor deletado")
        conexao.commit()
        print("deletados")

    



def menu():
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