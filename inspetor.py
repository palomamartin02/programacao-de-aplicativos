comprimento = input("Sua peça está no comprimento entre 10cm a 12cm? (S/N): ")
if comprimento == "S":
    print("comprimento válido!")
else:
    print("REPROVADO: Problema no comprimento")

largura = input("a largura está entre 5cm a 6cm? (S/N): ")
if largura == "S":
    print("peça aprovada!")
else:
    print("REPROVADO: Problema na largura")