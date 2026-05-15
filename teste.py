import json


frase = input("Digite uma frase: ")


dados = {
    "mensagem": frase
}


with open("teste.json", "w") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("Frase salva com sucesso em teste.json!")