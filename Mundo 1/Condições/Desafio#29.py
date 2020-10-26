velocidade = float(input('Qual é sua velocidade'))
if (velocidade>80):
    print('MULTADO! PASSOU DO LIMETE!')
    multa = (velocidade-80)*70
    print('A multa será de {:.2f} reais'.format(multa))
else:
    print('Esta tudo ok pode continuar')       