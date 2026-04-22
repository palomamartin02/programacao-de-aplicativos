senha = int(input("Digite a senha:" ))
def senha_valida(senha):
    if len(senha) > 6:
        return "True"
    else:
        return "False"
    while senha != "True":
        print("Senha incorreta.")
        senha = input("Digite a senha: ")
    if senha == "True":
        print("Senha cadastrada com sucesso!")
mensagem = senha_valida(senha)
print(mensagem)