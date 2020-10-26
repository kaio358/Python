matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somaTerceiraColuna = 0
maior = 0
for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int(input(f'Na posição [{linha}][{coluna}] : '))
        soma += matriz[linha][coluna]
        if coluna == 2:
            somaTerceiraColuna += matriz[linha][coluna]
        if linha == 1 : 
            if matriz[linha][coluna]>maior:
                maior = matriz[linha][coluna]
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()
print('Soma de todos valores',soma)
print('Soma da terceira coluna',somaTerceiraColuna)
print('O maior numero da segunda linha é',maior)