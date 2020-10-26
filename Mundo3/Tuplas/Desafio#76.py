listaDePreco = ('Lapis',1.75,
                'Borracha',2,
                'Caderno',15.90,
                'Estojo',25,
                'Transferidor',4.50,
                'Compasso',9.99,
                'Mochila',120.32,
                'Canetas',22.39,
                'Livro',34.90)
print('-'*40)
print(f'{"LISTA DE PREÇOS": ^40}')
print('-'*40)
for item in range(0,len(listaDePreco)):
    if item % 2 == 0 : 
        print(f'{listaDePreco[item]:.<30}',end='')
    else:
        print(f'R${listaDePreco[item]:>7.2f}')
print('-'*40)