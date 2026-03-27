clientes = ["luis", "ayumi", "mavi", "paulo", "aninha"]
cliente_atendido = []
cliente_atendido.append(clientes[0])
clientes.pop(0)
while len (clientes) >= 1:
    print(f"{cliente_atendido} foi atendido.")
    break