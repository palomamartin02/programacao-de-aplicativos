id = int(input("Digite seu id (0,1 ou 2): "))
temperatura = float(input("Digite a temperatura da máquina: "))
uso = int(input("Digite as horas de uso: "))

#LIMPEZA
if (id & 3 == 0) and (temperatura > 40) or uso > 8: 
    print(f"Funcionário {id}, você foi escalado para a manutenção preventina hoje.")

else:
    print(f"Funcionário {id}, sua máquina opera dentro dos padrões normais.")