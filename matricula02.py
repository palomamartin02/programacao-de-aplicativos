import json
import os

BANCO_DADOS = "alunos02.json"

def cadastrar():
    print("\n--- Novo Cadastro ---")

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)
