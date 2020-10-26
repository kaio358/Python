lista = []
listaPar = []
listaImpar = []
continuar ='s'
while continuar in 'Ss':
    valor = int(input('Insira o seu numero : '))
    lista.append(valor)
    if valor % 2 == 0 :
        listaPar.append(valor)
    if valor % 2 == 1 :
        listaImpar.append(valor)
    continuar = str(input('Continuar [S/N] ?'))
print('Lista completa',lista)
print('Lista par',listaPar)
print('Lista impar : ',listaImpar)