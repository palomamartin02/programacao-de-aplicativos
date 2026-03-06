print("BEM VINDO AO SISTEMA DE POUSO!")

#  FASE DE IDENTIFICAÇÃO:
codigo = int(input("Digite o código do drone: "))
autorizacao = input("Possui Autorização da Torre? (s/n): ")

if codigo == 999 and autorizacao == "s":
    print("Acesso liberado: avançe para a análise de pouso!")
    # FASE DE ANÁLISE DE VOO:
    nivel_de_bateria = int(input("Digite o nível de bateria (0 a 100): "))
    clima = input("Como está o clima hoje? (ensolarado/chuvoso): ")
    velocidade_do_vento = int(input("Velocidade do vento (km/h): "))
 
    # EMERGÊNCIA
    if nivel_de_bateria < 10:
        print("POUSE IMEDIATAMENTE!")

    # POUSO SEGURO
    elif nivel_de_bateria >= 10: 
        if (clima == "ensolarado" and velocidade_do_vento < 30) or (clima == "chuvoso" and velocidade_do_vento < 10 ):
            print("POUSO AUTORIZADO: Iniciando descida.")
  
        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita")

else:
    print("ERRO 01: Drone não identificado. Retornando à base.")
    


