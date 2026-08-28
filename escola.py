import sqlite3
from banco import conectar


def cadastrar_escola():
    nome = input("Nome da escola: ")
    cidade = input("Cidade: ")

    assert nome != "", "O nome da escola não pode ficar vazio."
    assert cidade != "", "A cidade não pode ficar vazia."

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO escolas (nome, cidade) VALUES (?, ?)",(nome, cidade))

        conexao.commit()
        conexao.close()

        print("Escola cadastrada com sucesso!")

    except sqlite3.Error as erro:
        print("Erro:", erro)


def listar_escolas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        for escola in escolas:
            print(escola)

        conexao.close()

    except sqlite3.Error as erro:
        print("Erro:", erro)


def alterar_escola():
    try:
        id_escola = int(input("ID da escola: "))
    except ValueError:
        print("Digite um ID válido.")
        return

    nome = input("Novo nome: ")
    cidade = input("Nova cidade: ")

    assert nome != "", "O nome da escola não pode ficar vazio."
    assert cidade != "", "A cidade não pode ficar vazia."

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?",(nome, cidade, id_escola))

        conexao.commit()
        conexao.close()

        print("Escola alterada com sucesso!")

    except sqlite3.Error as erro:
        print("Erro:", erro)


def excluir_escola():
    try:
        id_escola = int(input("ID da escola: "))
    except ValueError:
        print("Digite um ID válido.")
        return

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM escolas WHERE id = ?",(id_escola,))

        conexao.commit()
        conexao.close()

        print("Escola excluída com sucesso!")

    except sqlite3.Error as erro:
        print("Erro:", erro)
