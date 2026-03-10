numero_total =int(input("Digite o número total de garrafas que já passaram pela esteira hoje: "))

if numero_total == 500:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!") 
    print("QUALIDADE: Retirar amostra para teste.")

# ALERTA DE LIMPEZA
elif numero_total % 500 == 0: 
    print("HORA DA LIMPEZA: Parar máquina imediatamente! ")

# CONTROLE DE QUALIDADE
elif numero_total % 100 == 0:
    print("QUALIDADE: Retirar amostra para teste.")

   
#PRODUÇÃO NORMAL
else:
    print(" Produção em dia. Garrafa número [X] processada.")