# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
from copy import deepcopy
novos_produtos = deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] *= 1.10

produtos_ordenados_por_nome = deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda x:x['nome'], reverse=True)

produtos_ordenados_por_preco = deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x:x['preco'])

print('precos +10')
for k in novos_produtos:
    print(k)
print()
print('ordenados por nome')
for i in produtos_ordenados_por_nome:
    print(i)
print()
print('produtos ordenados por preço')
for j in produtos_ordenados_por_preco:
    print(j)