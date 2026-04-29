def sofrer_dano(vida_atual, valor_dano):
    nova_vida = vida_atual - valor_dano
    return nova_vida

vida = 100

print(f"Vida inicial: {vida}")

while vida > 0:
    dano = int(input("Quanto de dano o monstro causou? "))
    vida = sofrer_dano(vida, dano)
    
    if vida > 0:
        print(f"Vida restante: {vida}")
    else:
        print("Vida: 0")

print("Game Over")