senha = (input("Digite a senha: "))
tentativa = int(input("Digite o número da tentativa atual: ")) 
token = input("possui token especial VIP (s/n)?: ")

#ACESSO
if (senha == "admin123") and (tentativa & 3 == 0) or token == "s":
    print(f"Tentativa n° {tentativa}: ACESSO CONCEDIDO")

else:
    print(f"Tentativa n° {tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")