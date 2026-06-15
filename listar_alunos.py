import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM alunos")

alunos = cursor.fetchall()

print("\n LISTA DE ALUNOS:  ")
for aluno in alunos:
    print(alunos)

conexao.close()