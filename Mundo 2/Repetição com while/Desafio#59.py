from time import sleep
numeroUm = float(input('Informe o primeiro valor : '))
numeroDois = float(input('Informe o segundo valor : '))
escolha = 0
while escolha != 5 :
    print('Escolha o tipo de calculo : ')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] outros numeros ')
    print('[5] sair ')
    escolha = int (input('Informe a sua escolha : '))
    if escolha == 1:
        print('{} + {} = {}'.format(numeroUm,numeroDois,numeroUm+numeroDois))
    elif escolha == 2:
        print('{} X {} = {}'.format(numeroUm,numeroDois,numeroUm*numeroDois))
    elif escolha == 3:
        if numeroUm > numeroDois:
            print(numeroUm,'É maior')
        elif numeroDois > numeroUm:
            print(numeroDois,'É maior')
        else:
            print('São iguais')
    elif escolha == 4 :
        numeroUm = float(input('Informe o novo valor do primeiro : '))
        numeroDois = float(input('Informe o novo valor do segundo : '))
    elif escolha not in (0,5):
        print('Não existe essa escolha')
    print('-=-'*10)
    sleep(1.5)
print('Saiu !')