mostrar_menu = 'MENU'
while True:
        print('='*25)
        print(f'{mostrar_menu:^25}')
        print('='*25)
        print('\n' \
        '[ 1 ] Ver se o numero é par ou impar \n'
        '[ 2 ] Ver se o numero é positivo ou negativo \n'
        '[ 3 ] Ver se o numero é multiplo de 5 \n'
        '[ 0 ] Sair ')
        print('='*25)
        opções = input('Digite uma das opções acima: ')

        if opções == '0':
                print('Saindo do jogo.')
                break
        try:
                if opções == '1':
                        numero_1 = int(input('Digite o numero: '))
                        if numero_1%2==0:
                                print(f'o numero {numero_1} é par.')
                        else:
                                print(f'o numero {numero_1} é impar')
                        continue
                if opções == '2':
                        numero_2 = int(input('Digite o numero: '))
                        if numero_2 >= 0:
                                print(f'o numero {numero_2} é positivo.')
                        else:
                                print(f'O numero {numero_2} é negativo')
                        continue
                if opções == '3':
                        numero_3 = int(input('Digite o numero: '))
                        if numero_3 % 5 == 0:
                                print(f'O numero {numero_3} é divisivel por 5')
                        else:
                                print(f'O numero {numero_3} não é divisivel por 5')
                        continue
                if opções not in '123':
                        print('Opção invalida')
                print() 
        except ValueError:
                print('Digite apenas numeros')

'''JOGO DE OPÇÕES

🎯 Objetivo: Criar um programa com menu de opções, que executa ações diferentes conforme a escolha do usuário.
📌 Regras
O programa deve rodar em while True
Mostrar um menu assim:
========================
        MENU
========================
[ 1 ] Ver se o número é par ou ímpar
[ 2 ] Ver se o número é positivo ou negativo
[ 3 ] Ver se o número é múltiplo de 5
[ 0 ] Sair
========================

Validar a opção escolhida
Pedir um número (usar try / except)
Executar a lógica conforme a opção
Voltar ao menu até o usuário sair'''