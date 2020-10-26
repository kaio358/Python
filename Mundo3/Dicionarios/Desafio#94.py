lista = {}
pessoa = []
continuar = 's'

media = 0
while continuar in 'Ss':
    lista.clear()
    lista['nome'] = str(input('Nome : '))
    while True:
        lista['sexo'] = str(input('Sexo[M/F] : '))
        if (lista['sexo'] in 'MmFf'):
            break
        print('Erro!!')
    lista['idade'] = int(input('Idade : '))
    pessoa.append(lista.copy())
    media += lista['idade']
    while True:
        continuar = str(input('Continuar [S/N] ? '))
        if(continuar in 'SsNn'):
            break
print()
print(f'Existe no total de {len(pessoa)} pessoas')
media =media/len(pessoa)
print(f'A media de idade é {media:.2f}')
print('As mulheres são ',end =' ')
for cada in pessoa:
     if cada['sexo'] in 'Ff':
         print(cada['nome'],end=' ')
print()
for cada in pessoa:
    if cada['idade']>media:
        print(cada['nome'],';',cada['sexo'],';',cada['idade'])