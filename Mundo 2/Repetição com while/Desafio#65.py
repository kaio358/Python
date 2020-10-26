continuar = 's'
contadora = maior = menor = media = soma = 0
while continuar in'Ss':
    numero = int(input('Insira o valor desejado : '))
    contadora += 1
    soma += numero
    if contadora == 1:
        maior = numero
        menor = numero
    if numero > maior:
           maior = numero
    if numero < menor:
           menor = numero
   
    continuar = str(input('Continuar [S/N] ? '))
media = soma/contadora
print('O numero total digitado foi {} e a media {}'.format(contadora,media))
print('O maior e {} e o menor {}'.format(maior,menor))