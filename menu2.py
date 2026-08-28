from banco import inicializar_banco
from escola import (
    cadastrar_escola,
    listar_escolas,
    alterar_escola,
    excluir_escola
)

from turma import (
    cadastrar_turma,
    listar_turmas,
    alterar_turma,
    excluir_turma
)

from alunos import (
    cadastrar_aluno,
    listar_alunos,
    alterar_aluno,
    excluir_aluno
)


def menu_escolas():
    while True:
        print("\n===== MENU ESCOLAS =====")
        print("1 - Cadastrar escola")
        print("2 - Listar escolas")
        print("3 - Alterar escola")
        print("4 - Excluir escola")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_escola()

        elif opcao == "2":
            listar_escolas()

        elif opcao == "3":
            alterar_escola()

        elif opcao == "4":
            excluir_escola()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_turmas():
    while True:
        print("\n===== MENU TURMAS =====")
        print("1 - Cadastrar turma")
        print("2 - Listar turmas")
        print("3 - Alterar turma")
        print("4 - Excluir turma")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_turma()

        elif opcao == "2":
            listar_turmas()

        elif opcao == "3":
            alterar_turma()

        elif opcao == "4":
            excluir_turma()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_alunos():
    while True:
        print("\n===== MENU ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Alterar aluno")
        print("4 - Excluir aluno")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")

            try:
                idade = int(input("Idade: "))
                id_turma = int(input("ID da turma: "))
            except ValueError:
                print("Digite números válidos.")
                continue

            cadastrar_aluno(nome, idade, id_turma)

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            try:
                id_aluno = int(input("ID do aluno: "))
                idade = int(input("Nova idade: "))
                id_turma = int(input("Novo ID da turma: "))
            except ValueError:
                print("Digite números válidos.")
                continue

            nome = input("Novo nome: ")

            alterar_aluno(id_aluno, nome, idade, id_turma)

        elif opcao == "4":
            try:
                id_aluno = int(input("ID do aluno: "))
            except ValueError:
                print("Digite um ID válido.")
                continue

            excluir_aluno(id_aluno)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_principal():
    inicializar_banco()

    while True:
        print("\n==============================")
        print("       GESTÃO ESCOLAR")
        print("==============================")
        print("1 - Escolas")
        print("2 - Turmas")
        print("3 - Alunos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_escolas()

        elif opcao == "2":
            menu_turmas()

        elif opcao == "3":
            menu_alunos()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")



menu_principal()
menu_alunos()
menu_escolas()
menu_turmas()
