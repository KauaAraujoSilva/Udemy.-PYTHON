velocidade = 60
local_carro = 90
RADAR_1 = 60
LOCAL_RADAR = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('A velocidade ultrapassou')
    if local_carro >= (LOCAL_RADAR - RADAR_RANGE) and local_carro <=(LOCAL_RADAR + RADAR_RANGE):
        print('Carro multado')
else:
    print('Dentro da velocidade permitida')