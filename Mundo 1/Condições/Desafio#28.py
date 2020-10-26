from random import randint
computador = randint(0,5)
print('-=-'*10)
print('Tente adivinhar o numero entre 0 a 5 ')
print('-=-'*10)
jogador = int(input('Insira o numero desejado : '))
if jogador == computador:
    print('Acertou mizeravel ')
else:
    print('ERROU')