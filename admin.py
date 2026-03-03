usuario  = input("digite o nome de usuário: ")
senha = int(input("digite a senha: "))

if (usuario == "admin" or usuario == "root") and senha == 12345:
    print(" Acesso liberado!")

elif (usuario != "admin" or usuario != "root") and senha != 12345:
    print("Acesso negado!")