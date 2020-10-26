def ajudaPython (informar):
    
    frase = str()
    comeco = 'Sistema de ajuda Python'
    tamanho = len(comeco)
    print('\033[42m~'*tamanho)
    print(f'{comeco}')
    print('~'*tamanho)
    tamanho = len(informar)
    print('\033[m')
    if informar == 'fim':
        print('\033[41m~'*tamanho)
        print(f'{informar:^3}')
        print('~'*tamanho)
        print('\033[m')
    else:
         frase = 'Acesso ao Manual do '+informar
         tamanho = len(frase)
         print('\033[44m~'*tamanho)
         print(f'{frase}')
         print('~'*tamanho)
         print('\033[m')
         print('\033[31;46m',end ='')
         print(help(informar))
         print('\033[m')
         
#Principal
informar = ''
while True:
    informar = str(input('Funções ou Biblioteca > ')).lower()
    if informar == 'fim':
        ajudaPython(informar)
        break
    else:
        ajudaPython(informar)