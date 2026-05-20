import json


def criar_arquivo():
    open('matricula.json', 'w'). close()

def criar():
    nome_completo = input("Nome Completo: ")
    idade = int(input("Idade: "))
    cpff = int(input("CPF: "))
    turma = input("Turma: ")
    telefone = int(input("Telefone: "))
    with open ("matricula.json", 'a') as arquivo:
        matricula["nome"] = nome_completo,
        matricula["idad"] = idade,
        matricula["cpf"] = cpf,
        matricula["turm"] = turma,
        matricula["telef"] = telefone, 
        json.dump(alunos, arquivo, indent=4)
