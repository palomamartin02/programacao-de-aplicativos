nota = int(input("Digite sua nota: "))

def avaliar_desempenho (nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota > 5:
        return "Regular"   
    else:
        return "Insuficiente"
mensagem = avaliar_desempenho(nota)
print(mensagem)