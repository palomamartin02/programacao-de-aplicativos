def senha_valida(senha):
    if len(senha) > 6:
        return True
    else:
        return False

senha = input("Digite a senha: " )

while not senha_valida(senha):
    print("Senha incorreta.")
    senha = input("Digite a senha: ")
  
print("Senha cadastrada com sucesso!")