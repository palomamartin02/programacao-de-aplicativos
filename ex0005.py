def gerar_etiqueta(rua, num, bairro, cidade, cep, urgencia=False):
    
    texto = f"RUA: {rua}, {num} - {bairro}, {cidade} - {cep}"
    
    
    if urgencia == True:
        texto = "URGENTE! " + texto
        
    return texto


r = input("Rua: ")
n = input("Nº: ")
b = input("Bairro: ")
cid = input("Cidade: ")
cp = input("CEP: ")
u = input("Urgente? (s/n): ") == "s"


print(gerar_etiqueta(r, n, b, cid, cp, u))