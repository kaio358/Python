from random import randint
contadora = 0
while True:
    numero = int(input('Insira o valor da jogada : '))
    parOuImpar = str(input('Par ou Impar ? [P/I] '))
    computadorNumero = randint(0,10)
    if parOuImpar in 'Pp':
        if  (numero+computadorNumero)%2 == 0 :
            print('Wins!!')
            contadora+=1
        else:
            print('Derrota!!')
            break
    elif parOuImpar in 'Ii':
        if (numero+computadorNumero)%2 == 1:
            print('Wins!!')
            contadora+=1
        else:
            print('Derrota!!')
            break
print(f'Você venceu {contadora}')