import sqlite3
from banco import conectar


def cadastrar_turma():
    nome_turma = input("Nome da turma: ")

    try:
        id_escola = int(input("ID da escola: "))
    except ValueError:
        print("Digite um ID válido.")
        return

    assert nome_turma != "", "O nome da turma não pode ficar vazio."
    assert id_escola > 0, "O ID da escola deve ser maior que zero."

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)",
            (nome_turma, id_escola)
        )

        conexao.commit()
        conexao.close()

        print("Turma cadastrada com sucesso!")

    except sqlite3.Error as erro:
        print("Erro: a escola informada não existe.")
        print(erro)


def listar_turmas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        for turma in turmas:
            print(turma)

        conexao.close()

    except sqlite3.Error as erro:
        print("Erro:", erro)


def alterar_turma():
    try:
        id_turma = int(input("ID da turma: "))
        id_escola = int(input("Novo ID da escola: "))
    except ValueError:
        print("Digite números válidos.")
        return

    nome_turma = input("Novo nome da turma: ")

    assert nome_turma != "", "O nome da turma não pode ficar vazio."
    assert id_escola > 0, "O ID da escola deve ser maior que zero."

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("UPDATE turmas SET nome_turma = ?, id_escola = ? WHERE id = ?", (nome_turma, id_escola, id_turma))

        conexao.commit()
        conexao.close()

        print("Turma alterada com sucesso!")

    except sqlite3.Error as erro:
        print("Erro: a escola informada não existe.")
        print(erro)


def excluir_turma():
    try:
        id_turma = int(input("ID da turma: "))
    except ValueError:
        print("Digite um ID válido.")
        return

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM turmas WHERE id = ?", (id_turma,))

        conexao.commit()
        conexao.close()

        print("Turma excluída com sucesso!")

    except sqlite3.Error as erro:
        print("Erro:", erro)
