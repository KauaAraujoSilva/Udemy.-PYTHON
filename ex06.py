# ler um nome e deixar do jeito abaixo: 
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'

nome = str(input('Digite o seu nome: '))
contador = 0
while contador < len(nome):
    print(f'*{nome[contador]}', end='')
    contador+=1