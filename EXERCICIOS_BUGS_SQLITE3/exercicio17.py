import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 

        cursor.execute("INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) ## Erro: o correto é INSERT.
        conexao.commit() 
    except sqlite3.Error: 
        print("Erro: Este CPF já está cadastrado no sistema!") 

    finally: 
        conexao.close()


# CODIGO CORRIGIDO

def inserir_professor(nome, materia, cpf):
    try:
        conexao = sqlite3.connect("sistema_escola.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO professores (nome, materia, cpf) VALUES (?, ?, ?)",
            (nome, materia, cpf)
        )

        conexao.commit()
        print("Professor cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: Este CPF já está cadastrado no sistema!")

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

    finally:
        conexao.close()