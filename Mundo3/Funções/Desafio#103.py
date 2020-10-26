def ficha(nome ='<desconhecido>',gols = 0):
    return f'O jogador {nome} marcou {gols} gol(s)'

nome = str(input('Insira o nome : '))
gol = str(input('Gols : '))
if gol.isnumeric():
    gols = int(gol)
else:
    gol = 0
if nome.strip() == '':
    print(ficha(gols = gol))
else:
    print(ficha(nome,gols))