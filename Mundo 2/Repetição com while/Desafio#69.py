contadoraMulher = contadoraDeMaior = contadoraDeHomem = 0
while True:
    idade = int(input('Informe a idade : '))
    sexo = str(input('Informe o sexo [M/F] : '))
    if idade > 18:
        contadoraDeMaior +=1
    if sexo in 'Mm':
        contadoraDeHomem += 1
    if sexo in 'Ff':
        if idade < 20 :
            contadoraMulher += 1
    continuar = str(input('Continuar [S/N] ? '))
    if continuar in'Nn':
       break
print(f'Total de Maior de 18 anos são {contadoraDeMaior}')
print(f'Total de mulher abaixo dos 20 anos são {contadoraMulher}')
print(f'Total de homens são {contadoraDeHomem}')