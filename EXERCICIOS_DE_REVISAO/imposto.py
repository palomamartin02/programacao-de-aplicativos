salarios = [1500, 2500, 3500, 4500]
impostos = []

for salario in salarios:
    if salario <= 2000:
        imposto = salario * 0.10

    else:
        imposto = salario * 0.20
    impostos.append(imposto)
    print(f"Salário: R${salario} | Imposto: R${imposto} ")