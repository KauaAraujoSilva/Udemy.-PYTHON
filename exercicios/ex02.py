n = input('Digite um numero: ')
if n.isdigit():
    n_int = int(n)
    print(f'O seu numero é {n} e seu dobro é {n_int*2}')
else:
    print('O valor não é um numero')