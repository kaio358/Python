lista = []
continuar ='s'
while continuar in 'Ss':
    lista.append(int(input('Insira o primeiro valor : ')))
    continuar = str(input('Continuar [S/N] ?'))
print(f'No total de numeros criados foram de {len(lista)}')
lista.sort(reverse = True)
print(lista)
if 5 in lista:
    print('O numero 5 faz parte da lista')
else:
    print('O numero 5 não faz parte da lista')