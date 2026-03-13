# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
    
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('Joao', 32)
p2 = Pessoa('Arthur', 23)
p3 = Pessoa('Matheus', 12)

Unir_listas = [p1.__dict__, vars(p2), p3.__dict__]

CAMINHO_ARQUIVO = 'ex015.json'
with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(Unir_listas, arquivo, indent=2)
    
if __name__ == '__main__':
    print('é o main')