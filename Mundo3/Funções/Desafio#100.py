from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteio dos numeros ')
    for contador in range (0,6):
        num = randint(1,10)
        lista.append(num)
        print(f'{num}',end=' ')
        sleep(0.3)
    print('Ai está ')
def somarPar (lista):
    soma = 0
    for valor in lista:
        if valor %2 ==0:
            soma += valor
    print('Soma dos numeros pares são',soma)
numeros = list()
sorteio(numeros)
somarPar(numeros)