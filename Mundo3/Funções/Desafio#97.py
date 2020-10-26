def escreva (texto):
    tamanho = len(texto)
    print('-'*tamanho)
    print(f'{texto:^2}')
    print('-'*tamanho)
escreva(input('Informe o seu texto : '))