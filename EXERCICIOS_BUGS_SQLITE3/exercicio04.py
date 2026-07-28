import sqlite3 
 
def cadastrar_escola_rapido(): 
    nome = input("Digite o nome da escola: ") 
    endereco = input("Digite o endereço: ") 
     
    conexao = sqlite3.connect('sistema_escola.db')  
    cursor = conexao.cursor() 
     
	# Erro: SQL Injection.
    # Os valores do usuário estão sendo colocados diretamente dentro do comando SQL. 
    cursor.execute(f"INSERT INTO escolas (nome, endereco) VALUES ('{nome}', '{endereco}')") 
     
    conexao.commit() 
    conexao.close()


# CODIGO CORRIGIDO

def cadastrar_escola_rapido():
    nome = input("Digite o nome da escola: ")
    endereco = input("Digite o endereço: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO escolas (nome, endereco) VALUES (?, ?)",
        (nome, endereco)
    )

    conexao.commit()
    conexao.close()