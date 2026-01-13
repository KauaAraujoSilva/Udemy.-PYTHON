"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um numero inteiro: ')

if num.isdigit():
    numint = int(num)
    if numint%2==0:
        print('Esse numero é par!')
    else:
        print('Esse numero é impar!')
else:
    print('Você não digitou um numero')

'''else:
    print('Esse numero não é inteiro') ''' #não esta funcionando essa parte, para verificar se o num é int

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

'''hora = int(input('Digite que horas são: '))
if 0<hora<=11:
    print('Bom dia!')
elif 12<hora<=17:
    print('Boa tarde!')
elif 18<hora<=23:
    print('Boa noite!')'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''nome = input('Digite o seu nome: ')
ler_nome = len(nome)
if 0<ler_nome<=4:
    print('Seu nome é muito pequeno!')
elif 5<=ler_nome<6:
    print('Seu nome é mediano') 
elif ler_nome>=6:
    print('Seu nome é muito grande!')'''