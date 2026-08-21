# EXERCICIO 01

def dobrar(numero):
 	return numero * 2

assert dobrar(3) == 6   #P
assert dobrar(0) == 1   #F
assert dobrar(-2) == -4 #P

# REGISTRO:
# O segundo assert falhou
# O resultado real: 0
# A expectativa estava incorreta porque a função multiplica 0 por 2,
# então o resultado correto é 0, e não 1









# EXERCICIO 02

def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"

assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

# TESTE EXTRA
assert situacao_aluno(4) == "Reprovado"


# REGISTRO:
# 6 e 5.9 são casos de limite porque estão próximos da média mínima.
# A média 6 é o limite para ser aprovado, enquanto 5.9 está logo abaixo.









# EXERCICIO 03

def calcular_desconto(preco, percentual):
 	return preco - percentual

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45


# A função estava errada porque estava apenas subtraindo o percentual.
# O correto é calcular o valor do desconto em porcentagem.


# FUNÇÃO CORRIGIDA:
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


# Depois da correção, os testes passam:
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45











# EXERCICIO 04

def eh_par(numero):
 	return numero % 2 == 0

assert eh_par(3) is True

# O problema está no teste, não na função.
# O número 3 é ímpar, então o resultado correto é False.

# TESTE CORRIGIDO:
assert eh_par(3) is False

# JUSTIFICATIVA:
# A função está correta, pois 3 não é divisível por 2.










# EXERCICIO 05

def frete_gratis(valor):
 	return valor >= 200

def pode_votar(idade):
 	return idade >= 16

def senha_valida(senha):
 	return len(senha) >= 8

# Frete grátis
assert frete_gratis(199.99) is False
assert frete_gratis(200) is True
assert frete_gratis(200.01) is True


# Votação
assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True


# Senha
assert senha_valida("1234567") is False
assert senha_valida("12345678") is True
assert senha_valida("123456789") is True












# EXERCICIO 06

def situacao_faltas(faltas):
    if faltas <= 4:
        return "Regular"
    elif faltas <= 10:
        return "Atenção"
    else:
        return "Reprovado por falta"
	 
 	
# TESTES OBRIGATÓRIOS
assert situacao_faltas(0) == "Regular"
assert situacao_faltas(4) == "Regular"
assert situacao_faltas(5) == "Atenção"
assert situacao_faltas(10) == "Atenção"
assert situacao_faltas(11) == "Reprovado por falta"










# EXERCICIO 07

# FUNÇÃO ESCOLHIDA: desconto
# REGRA ENCONTRADA: calcular o desconto em porcentagem.

def calcular_desconto(preco, percentual):
    return preco - percentual

# TESTES
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

# FUNÇÃO CORRIGIDA
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

# TESTES CORRIGIDOS
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45









# EXERCICIO 08

def pode_votar(idade):
 	return idade >= 16

assert pode_votar(15) is False
assert pode_votar(16) is True

# TESTE EXTRA
assert pode_votar(17) is True









# EXERCICIO 09

def buscar_nome(lista, nome):
 	return nome in lista

def tem_senha_valida(senha):
 	return len(senha) >= 8

# Testes para buscar_nome
assert buscar_nome(["Ana", "João"], "Ana") is True
assert buscar_nome([], "Ana") is False
assert buscar_nome(["Ana"], "João") is False


# Testes para tem_senha_valida
assert tem_senha_valida("1234567") is False
assert tem_senha_valida("12345678") is True
assert tem_senha_valida("123456789") is True


# Em uma lista vazia, qualquer nome buscado não será encontrado.
# Por isso, o resultado é False.












# EXERCICIO 10

def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"
    
assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(15) == "Agradável"
assert classificar_temperatura(20) == "Agradável"
assert classificar_temperatura(25) == "Agradável"
assert classificar_temperatura(26) == "Quente"