def esta_na_lista(lista, nome_busca):
    for item in lista:
        if item == nome_busca:
            return "Encontrado!"
    return "Não disponível"

ferramentas = ["Martelo", "Chave de Fenda", "Alicate", "Furadeira"]

print(f"Buscando 'Alicate': {esta_na_lista(ferramentas, 'Alicate')}")

print(f"Buscando 'Linha': {esta_na_lista(ferramentas, 'Linha')}")