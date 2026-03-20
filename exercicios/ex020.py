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
# import math
# class Forma:
#     def area(self):
#         pass
    
# class Retangulo(Forma):
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura
        
#     def area(self):
#         return self.largura*self.largura
# class Circulo(Forma):
#     def __init__(self, raio):
#         self.raio = raio
        
#     def area(self):
#         return math.pi * self.raio**2
    
# r = Retangulo(11, 24)
# c = Circulo(4)
# print(r.area())
# print(c.area())

# Crie uma classe Forma com um método area(). Depois crie duas subclasses:
# Cada uma deve sobrescrever area() com o cálculo correto.
# r = Forma(4, 5).Area().Retangulo()
# c = Circulo(3)
# print(r.area())  # 20
# print(c.area())  # 28.27...



# 🎮 Exercício 4 — RPG Simples
# Crie uma classe Personagem com nome, vida e ataque. Implemente:
# class Personagem:
#     def __init__(self, nome, vida, ataque):
#         self.nome = nome
#         self.vida = vida
#         self.ataque = ataque
        
#     def estar_vivo(self):
#         if self.vida>0:
#             return True
#         print('O inimigo foi derrotado!')
        
#     def atacar_inimigo(self, outro):
#         outro.vida -= self.ataque
#         print(f'O inimigo sofreu um ataque!')
    
#     def __str__(self):
#         return f'Nome: {self.nome}  |  Vida: {self.vida}'
        
# class Heroi(Personagem):
#     def __init__(self, nome, vida, ataque, atacar_inimigo):
#         super().__init__(nome, vida, ataque, atacar_inimigo)
        
# class Inimigo(Personagem):
#     def __init__(self, nome, vida, ataque):
#         super().__init__(nome, vida, ataque)

# heroi = Personagem('Sir Vinland', 65, 25)
# print(heroi) # print(heroi.estar_vivo())
# inimigo = Personagem("Goblin", vida=60, ataque=15) 
# print(inimigo)

# heroi.atacar_inimigo(inimigo)
# print(inimigo)
# print(inimigo.estar_vivo())



# 🔒 Exercício 5 — Encapsulamento
# Crie uma classe Produto com os atributos privados _nome e _preco. Use properties para:
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor 
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, valor):
        if valor <0:
            raise ValueError('valor negativo')
        self._preco = valor
        
p = Produto('Notebook', 3500)
print(p.preco)
# p.preco = -100 #Da erro aqui!
# print(p.preco)
