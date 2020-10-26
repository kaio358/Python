def leiaInt(texto):
    booleano = True
    valor = 0
    while booleano:
        numero = str(input(texto))
        if numero.isnumeric():
            valor = int(numero)
            booleano = False
        else:
            print('\033[033m ERRO! Numero não é inteiro !\033[m')
    return valor
numero = leiaInt('Informe o numero : ')
print(f'Digitou um numero inteiro que é {numero}')