import sqlite3
from produtoras import inicializar_banco, cadastrar_produtora, listar_produtoras, atualizar_produtora, excluir_produtora

conexao = sqlite3.connect("show.db")
conexao.execute("PRAGMA foreign_keys = ON;")
cursor = conexao.cursor()


def inicializar_banco():
  
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtoras(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                razao_social TEXT NOT NULL,
                telefone_comercial TEXT NOT NULL UNIQUE
            )
        ''')
    
    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)

    return conexao



    
def cadastrar_produtora():
    try:
        razaosocial = input("RAZÃO SOCIAL: ")
        telefonecomercial = input("TELEFONE COMERCIAL: ")

        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtoras (razao_social, telefone_comercial) VALUES (?, ?)", (razaosocial, telefonecomercial)) 

        conexao.commit()
        print("Produtora cadastrada com sucesso!")


   
    except sqlite3.Error as erro:
        print("Erro no banco:", erro)






def listar_produtoras():
    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM produtoras")

        produtoras = cursor.fetchall()

        print("\n LISTA DE PRODUTORAS:  ")
        for produtora in produtoras:
            print(produtora)

    except sqlite3.Error as erro:
        print("Não foi possível listar as produtoras:", erro)






def atualizar_produtora():
    try:
        cursor = conexao.cursor()


        id_produtora = int(input("Digite o ID da produtora: "))

        nova_razao_social = input("NOVA RAZÃO SOCIAL: ")
        novo_telefone_comercial = input("NOVO TELEFONE COMERCIAL: ")

        cursor.execute( 
            "UPDATE produtoras SET razao_social = ?, telefone_comercial = ? WHERE id = ?", (nova_razao_social, novo_telefone_comercial, id_produtora))
        
        conexao.commit()
        print("Produtora atualizada com sucesso!")

    except ValueError:
        print("ID inválido! Digite um número inteiro.")

    except sqlite3.Error as erro:
        print("Não foi possível atualizar a produtora:", erro)





def excluir_produtora():
    try:
        cursor = conexao.cursor()


        id_produtora = int(input("Digite o ID da produtora: "))

        cursor.execute("SELECT id FROM produtoras WHERE id = ?", (id_produtora,))
        produtora = cursor.fetchone()

        if not produtora:
            print ("Produtora não encontrada ")
        else:
            cursor.execute("DELETE FROM produtoras WHERE id = ?", (id_produtora,))


            conexao.commit()
            print("Produtora deletada com sucesso!")

    
    except ValueError:
        print("ID inválido! Digite um número inteiro.")

    except sqlite3.Error as erro:
        print("Não foi possível excluir a produtora:", erro)