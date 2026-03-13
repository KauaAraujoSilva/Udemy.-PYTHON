# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qntd_acertos=0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    opções = pergunta['Opções']

    for v, opção in enumerate (opções):
        print(f'{v}) {opção}')

    escolha = input('Digite uma das opções: ')
    acertou = False
    escolha_int=None
    quantidade_de_opções = len(opções)

    if escolha.isdigit():
        escolha_int=int(escolha)

    if escolha_int is not None:
        if escolha_int>=0 and escolha_int < quantidade_de_opções:
            if opções[escolha_int] == pergunta['Resposta']:
                acertou=True
    print()

    if acertou:
        qntd_acertos+=1
        print('ACERTOUU!')
    else:
        print('Errou.')
    print()
print(f'Voce acertou {qntd_acertos} de {quantidade_de_opções-1} perguntas.')