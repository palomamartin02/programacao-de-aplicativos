nom = "Carlos"
lista =  [1200, 1500, 1100, 1900]
meta = 1400
    
def analisar_vendas(nome, lista_vendas, meta_mensal):
    soma = 0
    for m in lista_vendas:
        soma += m 

    quantidade_vendas = len(lista_vendas)
    media = soma / quantidade_vendas

    if media >= meta_mensal:
        return f"O vendedor {nome} teve média de {media} e bateu a meta"

    else:
        return f"O vendedor {nome} teve média de {media} e não bateu a meta"

resultado = analisar_vendas(nom, lista, meta)
print(resultado)


   
    


    