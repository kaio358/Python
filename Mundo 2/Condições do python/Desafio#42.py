segmento1 = float(input('Insira o valor do segmento 1 : '))
segmento2 = float(input('Insira o valor do segmento 2 : '))
segmento3 = float(input('Insira o valor do segmento 3 : '))
if (segmento1<segmento2+segmento3) and (segmento2<segmento1+segmento3)and(segmento3<segmento2+segmento1):
    print('O segmentos podem forma um triangulo \n')
    if segmento1 == segmento2 == segmento3:
        print('Triangulo Equilâtero')
    elif segmento1 != segmento2 != segmento3 :
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isósceles')
else:
    print('Não pode forma um triangulo')