print("SEJA BEM-VINDO(A)!")

curso = input("você concluiu o Curso de Segurança? (s/n): ")
if curso == "n":
    print("ACESSO NEGADO! Faça o terinamento primeiro")

elif curso == "s":
 
  instrutor = input("o instrutor está presente na sala? (s/n): ")
  if instrutor == "s":
     print("ACESSO LIBERADO: Operação iniciada!")

  else:
     print("Aguarde o instrutor para ligar a máquina!")