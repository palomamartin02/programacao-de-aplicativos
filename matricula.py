import json


def criar_arquivo():
    open('matricula.json', 'w'). close()

def criar():
    nome_completo = input("Nome Completo: ")
    idade = int(input("Idade: "))
    cpff = int(input("CPF: "))
    turma = input("Turma: ")
    telefone = int(input("Telefone: "))
    aluno = {"nome": nome_completo,
            "idad": idade,
            "cpf": cpff,
            "turm": turma,
            "telef": telefone, }
    with open('matricula.json', 'a') as arquivo:
        json.dump(aluno, matricula.json, ident=4, ensure-ascii=false)


def listar_aluno():
     with open('matricula.json', 'r') as arquivo: