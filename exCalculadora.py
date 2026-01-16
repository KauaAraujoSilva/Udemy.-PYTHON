from time import sleep
while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador(+-*/): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos dos numeros não esta valido')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Digite apenas dos operadores permitidos.')
    elif len(operador) > 1:
        print('Digite apenas um dos operadores permitidos.')
    print('O resultado da sua conta está sendo processado... ')
    sleep(1)
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ',num_1_float + num_2_float)
    if operador == '-':
        print(f'{num_1_float} - {num_2_float} = ',num_1_float - num_2_float)
    if operador == '*':
        print(f'{num_1_float} * {num_2_float} = ',num_1_float * num_2_float)
    if operador == '/':
        print(f'{num_1_float} / {num_2_float} = ',num_1_float / num_2_float)
    sair = input('Deseja [s]air?: ').lower().startswith('s')
    if sair is True:
        break
print('Você saiu do sistema.')