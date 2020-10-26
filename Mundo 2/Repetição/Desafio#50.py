soma = 0
contador = 0
for contagem in range (1,7):
    numero = int(input('Informe os numeros : '))
    if numero % 2 == 0 :
        soma += numero
        contador += 1
print ('No total dos numeros somados foram {}, o resultado da soma {}'
       .format(contador,soma))