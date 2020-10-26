maior = 0
menor = 0
for contadora in range (1,6):
    peso = float(input('Pessoa n° {} peso : '.format(contadora)))
    if contadora ==1 :
        menor = peso
    if(peso>maior):
        maior = peso
    if peso< menor:
        menor = peso
print('O maior peso :',maior)
print('O menor peso :',menor)