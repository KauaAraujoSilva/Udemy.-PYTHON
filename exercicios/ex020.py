# exercicio 1

# class Animal:
#     def __init__(self, nome_animal, som_animal):
#         self._nome_animal = nome_animal
#         self._som_animal = som_animal
#     def falar(self,):
#         return print(f'{self._nome_animal} faz {self._som_animal}') 
# # Esperado:
# cachorro = Animal("Rex", "Au au")
# cachorro.falar()  # Rex faz Au au

# exercicio 2

# class ContaBancaria:
#     def __init__(self, titular_da_conta,):
#         self._titular_da_conta = titular_da_conta
#         self._depositar = None
#         self._saldo = 0
#         self._sacar = None
#     def extrato(self):
#         return print(f'Titular: {self._titular_da_conta} | Saldo: {self._saldo}')
#     def depositar(self, valor):
#         self._saldo += valor
#     def sacar(self, valor):
#         if self._saldo > valor:
#             self._saldo -= valor
#         else: print('Não permite saldo negativo')
        
# conta = ContaBancaria("Ana")
# conta.depositar(500)
# conta.sacar(200)
# conta.extrato()  # Titular: Ana | Saldo: R$ 300.00



# exercicio 3

class Forma:
    def __init__(self,):...
        

# Crie uma classe Forma com um método area(). Depois crie duas subclasses:

# Retangulo(largura, altura)
# Circulo(raio)

# Cada uma deve sobrescrever area() com o cálculo correto.
# r = Retangulo(4, 5)
# c = Circulo(3)
# print(r.area())  # 20
# print(c.area())  # 28.27...




# 🎮 Exercício 4 — RPG Simples
# Crie uma classe Personagem com nome, vida e ataque. Implemente:

# atacar(outro_personagem) — reduz a vida do alvo pelo valor de ataque
# esta_vivo() — retorna True se vida > 0
# __str__ — retorna "[nome] — Vida: [vida]"

# pythonheroi = Personagem("Arthur", vida=100, ataque=30)
# inimigo = Personagem("Goblin", vida=60, ataque=15)

# heroi.atacar(inimigo)
# print(inimigo)        # Goblin — Vida: 30
# print(inimigo.esta_vivo())  # True



# 🔒 Exercício 5 — Encapsulamento
# Crie uma classe Produto com os atributos privados _nome e _preco. Use properties para:

# Obter o nome e o preço
# Impedir que o preço seja negativo (lançar ValueError se tentar setar um valor < 0)

# pythonp = Produto("Notebook", 3500)
# print(p.preco)   # 3500
# p.preco = -100   # ValueError: Preço não pode ser negativo