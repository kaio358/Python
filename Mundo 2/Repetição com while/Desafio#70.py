totalGasto = 0
menorGasto = ''
contadora = 0
maisBarato = 0
while True:
    nome = str(input('Informe o nome do produto : '))
    preco = int(input('Informe o preço : '))
    if totalGasto == 0:
        maisBarato = preco
        menorGasto = nome
    totalGasto += preco
    if preco > 1000:
        contadora+=1
    if preco<maisBarato:
        maisBarato = preco
        menorGasto = nome
    continuar = input('Continuar [S/N] ? ')
    if continuar in 'Nn':
        break
print(f'Total gasto foi {totalGasto},com maiores de 1000 são {contadora}')
print(f'O mais barato foi {menorGasto} custando {maisBarato}')