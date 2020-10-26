pessoa =[]
lista = []
maior = menor = 0 
continuar = 's'
while continuar not in 'Nn':
    pessoa.append(str(input('Informe o nome : ')))
    pessoa.append(float(input('Informe o peso : ')))
    if maior == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    if pessoa[1]>maior:
        maior = pessoa[1]
    if pessoa[1] < menor:
        menor = pessoa[1]
    lista.append(pessoa [:])
    pessoa.clear()
    continuar = str(input('Continuar [S/N] ? '))
print(f'No total de pessoas cadastradas foi de {len(lista)}')
print(f'O maior peso é {maior}, essas pessoas são ',end='')
for contador in lista:
    if contador[1] == maior:
        print(f'{contador[0]} ',end=' ')
print(f'O menor peso é {menor}, essas pessoas são ',end='')
for contador in lista:
    if contador[1] == menor:
        print(f'{contador[0]} ',end=' ')        