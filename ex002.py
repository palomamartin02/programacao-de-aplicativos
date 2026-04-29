def calcular_area(largura, comprimento):
    novo_valor = largura * comprimento
    return novo_valor

contador = 1
while contador <= 3:
    print(f" Terreno {contador}")
    l = float(input("Digite a largura (m): "))
    c = float(input("Digite o comprimento (m): "))
    
    area = calcular_area(l, c)

    print(f"A área do terreno {contador} é: {area} m²")
    
    contador += 1