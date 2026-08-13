# LISTAR

import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM alunos")

alunos = cursor.fetchall()

print("\n LISTA DE ALUNOS:  ")
for aluno in alunos:
    print(alunos)

conexao.close()



# BUSCAR

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual seu ID: "))

    cursor.execute(f'''SELECT nome , cpf , telefone , idade , turma FROM alunos WHERE id = {id_aluno}''')
    
    aluno = cursor.fetchone()

    if not aluno:
        print(" Não encontrado ")
    else:
        print(f" Nome atual {aluno[0]} ")
        print(f" CPF atual {aluno [1]} ")
        print(f" Telefone atual {aluno[2]} ")
        print(f" Idade atual {aluno [3]} ")
        print(f" Turma atual {aluno [4]} ")

        nome_atualizado = input(" Atualize seu nome: ")
        cpf_atualizado = input(" Atualize seu CPF: ")
        telefone_atualizado = input(" Atualize se telefone: ")
        idade_atualizada = input(" Atualize sua idade: ")
        turma_atualizada = input(" Atualize sua turma: ")

        cursor.execute(f'''
                        UPDATE alunos
                        SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}', Telefone ='{telefone_atualizado}', Idade ='{idade_atualizada}', Turma ='{turma_atualizada}'
                    WHERE id ={id_aluno}
                        ''')
        conexao.commit()
        print(" Dados alterados ")

        conexao.close()



# DELETAR

  conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual ID deseja deletar: " ))

    # Verifica se o aluno existe
    cursor.execute(f'''SELECT id FROM Alunos WHERE Id = {id_aluno}''')
    aluno = cursor.fetchone()

    if not aluno:
        print ("Aluno não encontrado ")
    else:
        cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
        conexao.commit()
        print("aluno deletado")

        conexao.close()

alterar()