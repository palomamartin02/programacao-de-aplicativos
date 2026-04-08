compra = float(input("Digite o valor da compra: "))
if compra > 100:
    desconto = compra * 0.10
    total = compra - desconto
    print(f"Desconto aplicado! Sua compra ficou no total de {total} reais.")

else:
    print(f"Sua compra ficou no total de {compra} reais")