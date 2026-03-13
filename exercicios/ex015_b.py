from ex015_a import CAMINHO_ARQUIVO, Pessoa, Unir_listas
import json

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    for pessoa in pessoas:
        print(pessoa['nome'])