numero = int(input('Informe o numero : '))
totalDeNumeros = 0
for contador in range (1,numero+1):
    if numero % contador == 0 :
        print('\033[36m',end=' ')
        totalDeNumeros +=1
    else:
        print('\033[35m',end=' ')
    print(contador,end=' ')
print('\n \033[mo numero e {} é divisivel por {}'.format(numero,contador))
if totalDeNumeros == 2 :
    print('\n É primo')
else:
    print('\n Não é primo')