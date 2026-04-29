def  contar_caracteres(palavra):
    return len(palavra)

usuario = input("Digite o nome de usuário: ")

tamanho = contar_caracteres(usuario)

if tamanho < 5:
    print("Nome de usuário muito curto")
else:
    print("Nome aceito")