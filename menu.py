import sqlite3

import produtoras
import arenas_estadios


def inicializar_banco():

    try:
        conexao = sqlite3.connect("show.db")
        conexao.execute("PRAGMA foreign_keys = ON;")
        cursor = conexao.cursor()

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
        conexao.close()

        print("Banco de dados criado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)


def Menu():

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
                produtoras.cadastrar_produtora()

            elif opcao == 2:
                produtoras.listar_produtoras()

            elif opcao == 3:
                produtoras.atualizar_produtora()

            elif opcao == 4:
                produtoras.excluir_produtora()

            elif opcao == 5:
                arenas_estadios.cadastrar_arena()

            elif opcao == 6:
                arenas_estadios.listar_arenas()

            elif opcao == 7:
                arenas_estadios.atualizar_arena()

            elif opcao == 8:
                arenas_estadios.excluir_arena()

            elif opcao == 0:
                print("\nENCERRANDO SISTEMA....")
                break

            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite um número válido!")


inicializar_banco()
Menu()
