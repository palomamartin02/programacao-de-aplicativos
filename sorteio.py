id = int(input("Digite seu ID de usuário: "))
valor_da_compra = float(input("Digite o valor total da compra: "))

if id % 2 == 0 and valor_da_compra > 500:
    print(f"Parabéns, usuário {id}! Você ganhou um cupom para sua compra de R$ {valor_da_compra} ")

else:
    print(f"Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")
