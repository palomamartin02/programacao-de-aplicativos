def eh_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

valor = int(input("Digite um número: "))
mensagem = eh_par(valor)
print(f"Esse número é: {mensagem}")