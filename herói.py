ataque = float(input("digite o poder de ataque do herói"))
defesa = float (input("digite os pontos de defesa do vilão"))

dano = ataque - defesa 

if dano <= 0:
    print ("O vilão bloqueou o ataque! Dano: 0")
elif dano > 0:
    print ("Ataque crítico! Você causou dano ao de", dano)
    