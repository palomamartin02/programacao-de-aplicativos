import sqlite3
from banco import *

def cadastrar_aluno(nome, idade, id_turma):
    try:
        assert nome != "", "O nome não pode ficar vazio."
        assert idade >= 3, "A idade deve ser igual ou superior a 3 anos."

        conexao = sqlite3.connect("gestao_escolar.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?)",(nome, idade, id_turma))

        conexao.commit()
        conexao.close()

        print("Aluno cadastrado!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("Erro no banco:", erro)


def listar_alunos():
    try:
        conexao = sqlite3.connect("gestao_escolar.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM alunos")

        for aluno in cursor.fetchall():
            print(aluno)

        conexao.close()

    except sqlite3.Error as erro:
        print("Erro no banco:", erro)


def alterar_aluno(id, nome, idade, id_turma):
    try:
        assert nome != "", "O nome não pode ficar vazio."
        assert idade >= 3, "A idade deve ser igual ou superior a 3 anos."

        conexao = sqlite3.connect("gestao_escolar.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("UPDATE alunosSET nome = ?, idade = ?, id_turma = ?WHERE id = ?",(nome, idade, id_turma, id))

        conexao.commit()
        conexao.close()

        print("Aluno alterado!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("Erro no banco:", erro)


def excluir_aluno(id):
    try:
        conexao = sqlite3.connect("gestao_escolar.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM alunos WHERE id = ?",(id,))

        conexao.commit()
        conexao.close()

        print("Aluno excluído!")

    except sqlite3.Error as erro:
        print("Erro no banco:", erro)

inicializar_banco()