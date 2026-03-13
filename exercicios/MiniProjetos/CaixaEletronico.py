print('Digite apenas numeros multiplos de 10.')
while True:
    saque = input('Digite o valor de quanto deseja sacar: ')    
    try:
        saque_int = int(saque)  
    except ValueError:
        print('Digite apenas numeros.')
    if saque_int <= 0:
        print('Digite apenas valores positivos!')
    if saque_int % 10 != 0:
        print('Esse numero não é divisivel por 10')
        continue

    valor = saque_int
    print('Notas entregues:')

    notas_100 = valor // 100
    valor %= 100
    if notas_100 > 0:
        print(f'{notas_100} x 100')

    notas_50 = valor // 50
    valor %= 50
    if notas_50 > 0:
        print(f'{notas_50} x 50')
    notas_20 = valor // 20
    valor %= 20
    if notas_20:
        print(f'{notas_20} x 20')
    notas_10 = valor // 10
    valor %= 10
    if notas_10:
        print(f'{notas_10} x 10')

    sair_sistema = input('Deseja [s]air do sistema?: ').lower().startswith('s')
    if sair_sistema is True:
        break
    else:
        continue
print('Você saiu do sistema')