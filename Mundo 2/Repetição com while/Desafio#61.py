termo = int (input('Informe o termo : '))
razao = int(input('Informe a razão : '))
contadora = 1
while contadora <= 10 :
    print(termo,'->',end='')
    termo+=razao
    contadora+=1
print('Acabou')