import sqlite3

from produtoras import inicializar_banco_produtoras, cadastrar_produtora, listar_produtoras, atualizar_produtora, excluir_produtora
from arenas_estadios import inicializar_banco_arenas, cadastrar_arena, listar_arenas, atualizar_arena, excluir_arena


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

inicializar_banco_produtoras()
menu()