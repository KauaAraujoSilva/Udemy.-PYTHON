#exercicio 1
'''try:
    numero = int(input('Digite um numero: '))
    print(numero)
except ValueError:
    print('Você não digitou um numero!')'''

#exercicio 2
'''try:
    numero_um = int(input('Digite o primeiro numero: '))
    numero_dois = int(input('Digite o segundo numero:  '))
    divisao = numero_um/numero_dois
    print(f'a divisão deu {divisao:.1f}')
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except ValueError:
    print('Digite apenas numero!')'''

#exercicio 3
lista = []
posicao = []
for nome in range(5):
    nome = input('Digite seu nome: ')
    lista.append(nome)
try:
    posicao = int(input('Digite uma posição: '))
    print(lista[posicao])
except IndexError:
    print('posição errada')
except:
    print('Digite apenas numero.')