from random import randint
item = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)

print('-+-'*10)
print('\033[32mJO\033[33mKEN\033[34mPO \033[m')
print('-+-'*10)
print('\n Escolha : ')
print(' [0] para Pedra')
print(' [1] para Papel')
print(' [2] para Tesoura')
jogador = int(input('Informe a sua opção : '))
print('Computador jogou',item[computador])
print('Jogador jogou',item[jogador])
if computador == 0 :
    if jogador == 0:
        print('\033[34m EMPATE!!!')
    elif jogador == 1:
        print('\033[32m WINS!!!')
    elif jogador == 2: 
        print('\033[31m DEAFT!!!')
elif computador == 1 :
    if jogador == 0:
        print('\033[31m DEAFT!!!')
    elif jogador == 1:
        print('\033[34m EMPATE!!!')
    elif jogador == 2: 
        print('\033[32m WINS!!!')
elif computador == 2 : 
    if jogador == 0:
        print('\033[31m DEAFT!!!')
    elif jogador == 1:
        print('\033[32m WINS!!!')
    elif jogador == 2: 
        print('\033[34m EMPATE!!!')