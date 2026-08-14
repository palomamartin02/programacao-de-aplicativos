import sqlite3

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
    

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS arenas_estadios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_local TEXT NOT NULL,
                capacidade_maxima INTEGER NOT NULL,
                id_produtora INTEGER NOT NULL,
                FOREIGN KEY (id_produtora) REFERENCES produtoras(id)
            )
        ''')
    
        conexao.commit()
        print("Banco de dados criado com sucesso!")

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









def cadastrar_arena():
    try:
        cursor = conexao.cursor()


        nome_local = input("NOME DO LOCAL: ")
        capacidade_maxima = int(input("CAPACIDADE MÁXIMA: "))
        id_produtora = int(input("ID DA PRODUTORA: "))

        cursor.execute("SELECT id FROM produtoras WHERE id = ?", (id_produtora,)  )
        produtora = cursor.fetchone()

        if not produtora:
            print ("Produtora não encontrada")
        else:
            cursor.execute("INSERT INTO arenas_estadios (nome_local, capacidade_maxima, id_produtora) VALUES (?, ?, ?)", (nome_local, capacidade_maxima, id_produtora))
            conexao.commit()
            print("Arena cadastrada com sucesso!")

    except ValueError:
        print("Erro: digite números nos campos numéricos.")
    
    except sqlite3.Error as erro:
        print("Erro no banco:", erro)





def listar_arenas():
    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM arenas_estadios")

        arenas_estadios = cursor.fetchall()

        print("\n LISTA DE ARENAS/ESTADIOS:  ")
        for arena in arenas_estadios:
            print(arena)

    except sqlite3.Error as erro:
        print("Não foi possível listar a arena/estadio:", erro)





def atualizar_arena():
    try:
        cursor = conexao.cursor()

        id_arena = int(input("ID DA ARENA: "))
        novo_nome_local = input("NOVO NOME DO LOCAL: ")
        nova_capacidade_maxima = int(input("NOVA CAPACIDADE MÁXIMA: "))
        id_produtora = int(input("NOVO ID DA PRODUTORA: "))

        cursor.execute("SELECT id FROM produtoras WHERE id = ?", (id_produtora,))
        produtora = cursor.fetchone()

        if not produtora:
            print ("Produtora não encontrada")
        else:
            cursor.execute("UPDATE arenas_estadios SET nome_local = ?, capacidade_maxima = ?, id_produtora = ? WHERE id = ?", (novo_nome_local, nova_capacidade_maxima, id_produtora, id_arena))
            conexao.commit()
            print("Arena/Estadio atualizada(o) com sucesso!")

    except ValueError:
        print("Erro: digite números nos campos numéricos.")
    
    except sqlite3.Error as erro:
        print("Erro no banco:", erro)







def excluir_arena():
    try:
        cursor = conexao.cursor()


        id_arena = int(input("ID DA ARENA: "))


        cursor.execute("SELECT id FROM arenas_estadios WHERE id = ?", (id_arena,))
        arena = cursor.fetchone()

        if not arena:
            print("Arena/Estadio não encontrada(o)")
        else:
            cursor.execute("DELETE FROM arenas_estadios WHERE id = ?", (id_arena,))
            conexao.commit()
            print("Arena/Estadio deletada(o) com sucesso!")

    except ValueError:
        print("Erro: digite números nos campos numéricos.")
    
    except sqlite3.Error as erro:
        print("Erro no banco:", erro)




def menu():
    while True:
        try:
            print("\n1 - Cadastrar produtora")
            print("2 - Listar produtoras")
            print("3 - Atualizar produtora")
            print("4 - Excluir produtora")
            print("5 - Cadastrar arena")
            print("6 - Listar arenas")
            print("7 - Atualizar arena")
            print("8 - Excluir arena")
            print("0 - Sair")

            opcao = int(input("Escolha: "))


            if opcao == 1:
                cadastrar_produtora()
            elif opcao == 2:
                listar_produtoras()
            elif opcao == 3:
                atualizar_produtora()
            elif opcao == 4:
                excluir_produtora()
            elif opcao == 5:
                cadastrar_arena()
            elif opcao == 6:
                listar_arenas()
            elif opcao == 7:
                atualizar_arena()
            elif opcao == 8:
                excluir_arena()
            elif opcao == 0:
                print("\n ENCERRANDO SISTEMA....")
                break
            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite um número válido!")

inicializar_banco()
menu()