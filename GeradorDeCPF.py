from re import sub #importa uma classe que so permita numeros ate a quant. desejada
from sys import exit #sai do programa
entrada = input('Digite o CPF: ') 
cpf_enviado_pelo_usuario = sub(r'[^0-9]', '', entrada) 

entrada_sequencial = cpf_enviado_pelo_usuario[0] * len(cpf_enviado_pelo_usuario)
if cpf_enviado_pelo_usuario == entrada_sequencial:
    print('Os dados informados formam uma sequencia.')
    exit()

nove_digitos = cpf_enviado_pelo_usuario[:9] #coleta os 9 digitos do cpf
contador_regressivo = 10
resultado_digito1 = 0

for digito1 in nove_digitos:
    resultado_digito1 += int(digito1) * contador_regressivo
    contador_regressivo -= 1
digito1 = (resultado_digito1*10)%11
digito1 = digito1 if digito1 <=9 else 0

dez_digitos = nove_digitos + str(digito1) # coleta os 9 digitos, mais o novo gerado
contador_regressivo2 = 11
resultado_digito2 = 0
for digito2 in dez_digitos:
    resultado_digito2 += int(digito2) * contador_regressivo
    contador_regressivo2 -= 1
digito2 = (resultado_digito2 *10)%11
digito2 = digito2 if digito2 <=9 else 0

# Verifica se o CPF digitado é valido ou não.
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito1}{digito2}' 
if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(cpf_gerado_pelo_calculo, end=' - ')  
    print('Este CPF é valido')
else:
    print('CPF INVALIDO \nO CPF enviado é diferente do resultado')