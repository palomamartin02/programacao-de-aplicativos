valor_da_compra = float(input("digite o valor da compra: " ))
cliente_prime = input("cliente prime? (S/N): ")

frete = 50
if (valor_da_compra > 500) or cliente_prime == "S" and valor_da_compra > 100:
    frete = 0

    total_final = valor_da_compra = frete 


