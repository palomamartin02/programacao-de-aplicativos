nome_de_usuario = input("digite seu nome de usuário: ")
codigo_secreto = input("digite o código secreto: ")

if nome_de_usuario == "admin" and codigo_secreto == "999":
    print("Acesso ao servidor liberado. Sistema online.")

elif nome_de_usuario != "admin" and codigo_secreto != "999":
    print ("Falha na autenticação. Alerta de segurança ligado!")