import json

def ler():
    with open('dados.json', 'r', encoding= 'utf-8') as f:
        dados = json.load(f)
        return dados
