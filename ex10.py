vagas = ["Ocupado", "Livre", "Ocupado", "Livre"]
vaga = int(input("Digite o número de uma vaga (0 a 3): "))

if vaga % 2 == 0 and vagas[vaga] == "livre":
    print(f"Vaga autorizada para estacionar.")
else:
    print(f"Vaga {vaga} indisponível ou fora das regras.")