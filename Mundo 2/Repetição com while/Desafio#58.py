from random import randint
computador = randint(0,10)
jogador = int(input('Informe um numero de 0 a 10 : '))
contadora = 0
while jogador != computador:
    if (computador> jogador):
        print('Ops tente denovo, o numero é maior')
        contadora  += 1
    elif computador < jogador : 
        print('Ehhhhh menor =, tente denovo')
        contadora += 1
    jogador = int(input('Escolha outro numero : '))
print('Acerto, foi necessario repetir a escolha',contadora)