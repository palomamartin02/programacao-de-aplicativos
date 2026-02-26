nivel_atual = int(input("digite seu nível atual:"))
esferas = int(input("digite a quantidade de esferas coletadas:"))

if nivel_atual >= 20 and esferas > 50:
  print("Habilidade Super Salto desbloqueada!")

elif nivel_atual < 20 and esferas < 50:
  print("Requisitos insuficientes para nova habilidade.")