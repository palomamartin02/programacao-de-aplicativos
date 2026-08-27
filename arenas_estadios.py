import sqlite3



conexao = sqlite3.connect("show.db")
conexao.execute("PRAGMA foreign_keys = ON;")
cursor = conexao.cursor()


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