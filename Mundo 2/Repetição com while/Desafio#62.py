termo = int(input('Informe o termo : '))
razao = int(input('Informe a razão : '))
contadora = 1
total = 10
continuar = 1
while continuar != 0 :
    total += continuar
    while contadora <=total:
        print(termo,'->',end=' ')
        termo += razao
        contadora +=1
    print('PAUSA')
    continuar = int(input('Informe quantidade desejada para continuar : '))
print('No total de termos mostrados foi',total)