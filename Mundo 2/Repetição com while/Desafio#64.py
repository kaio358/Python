contadora = soma = 0
numero = int(input('Insira o numero [999 para sair] : '))
while numero != 999:
    soma+=numero
    contadora +=1
    numero = int(input('Insira o numero [999 para sair] : '))
print('No total de numeros foi {}, e a soma deu {}'.format(contadora,soma))