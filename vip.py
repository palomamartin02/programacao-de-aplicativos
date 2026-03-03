idade = int(input("digite a sua idade: "))
tem_ingresso = input("possui ingresso? (S/N): ")
esta_na_lista = input("está na lista? (S/N): ")

if (idade >= 18 and tem_ingresso == "S") or esta_na_lista == "S": 
    print ("acesso liberado!")

