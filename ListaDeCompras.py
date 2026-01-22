"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista = []
while True:
    Opções = input('Selecione uma opção \n' \
            '[i]nserir  [a]pagar  [l]istar: ').lower()
    if Opções == 'a':
        lista.clear()
    try:
        if Opções == 'l':
            print(lista)
            continue
        elif Opções == 'i':
            Opção_I = input('Digite o que dejesa inserir: ')
            lista.append(Opção_I)
            lista.count()
        elif lista is False:
            print('ista falsa')
    except ValueError:
        print('dnfiadjf')
    except TypeError:
        print('DJFHADIF')