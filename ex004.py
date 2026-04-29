def  somar_carrinho(lista_precos):
    total = 0
    for preco in lista_precos:
        total += preco
    
    if total > 500.0:
        total = total * 0.90 
        return total

produtos = [200.0, 150.0, 100.0, 100.0]

valor_final = somar_carrinho(produtos)

print(f"Total da compra: R$ {valor_final}")