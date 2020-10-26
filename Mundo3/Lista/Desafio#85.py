lista = [[],[]]
valor = 0
for contador in range(0,7):
    valor = (int(input('Informe o seu numero : ')))
    if (valor % 2 == 0):
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Valor pares {lista[0]}')
print(f'Valores impares {lista[1]}')