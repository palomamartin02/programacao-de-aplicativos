valor_total_da_compra = float(input("digite o valor total da compra"))
nome_do_cupom = input("digite o nome do cupom")
nome_do_cupom = "DEV10"
desconto = valor_total_da_compra * 0.10
novo_preço = valor_total_da_compra - desconto

if nome_do_cupom == "DEV10":
    print("cupom aplicado!", novo_preço)
else:
    print("cupom invalido", valor_total_da_compra)