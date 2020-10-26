dinheiro = int(input('Insira o valor da quantia : '))
cedulas = 50
totalDeCedulas = 0
while True:
    if  dinheiro >= cedulas:
        totalDeCedulas = dinheiro//cedulas
        dinheiro %= cedulas
    else:
        print(f'Total de cedulas {totalDeCedulas} do valor de R$ {cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        if dinheiro == 0:
           break