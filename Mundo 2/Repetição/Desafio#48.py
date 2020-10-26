soma = 0
contador = 0
for contagem in range (1, 501,2):
    if contagem % 3 == 0:
        soma = soma +contagem
        contador += 1
print(' O valores somados foram de',contador,'e o resultado da soma',soma)      