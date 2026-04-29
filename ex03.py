def aplicar_promocao(lista):
    nova_lista = []
    for preco in lista:
        if preco > 100.0:
            novo_preco = preco * 0.85
            nova_lista.append(novo_preco)
        else:
            nova_lista.append(preco)
    return nova_lista

compras = [150.0, 80.0, 200.0, 50.0]
lista_atualizada = aplicar_promocao(compras)

print(f"Lista original: {compras}")
print(f"Lista com descontos: {lista_atualizada}")