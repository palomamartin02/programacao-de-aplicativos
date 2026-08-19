# EXERCICIO01

def eh_par(numero):
    return numero % 2 == 0


assert eh_par(10) == True       
assert eh_par(7) == False       
assert eh_par(0) == True       
assert eh_par(-4) == True 

# EXERCICIO 02

def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"


assert situacao_aluno(8) == "Aprovado"        
assert situacao_aluno(6) == "Aprovado"        
assert situacao_aluno(4) == "Recuperação"    
assert situacao_aluno(3) == "Reprovado"     
assert situacao_aluno(5.9) == "Recuperação" 

# EXERCICIO 03

def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


assert calcular_desconto(100, 0) == 100
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 50) == 100
assert calcular_desconto(150, 100) == 0
assert round(calcular_desconto(99.90, 10), 2) == 89.91


# EXERCICIO 04

def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False


assert pode_entrar(20, False) == True   
assert pode_entrar(16, True) == True   
assert pode_entrar(16, False) == False 
assert pode_entrar(18, False) == True   
assert pode_entrar(17, True) == True   

# EXERCICIO 05

def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20


assert calcular_frete(50) == 20    
assert calcular_frete(100) == 10   
assert calcular_frete(150) == 10   
assert calcular_frete(200) == 0    
assert calcular_frete(250) == 0   

print("Testes concluídos com sucesso!")


