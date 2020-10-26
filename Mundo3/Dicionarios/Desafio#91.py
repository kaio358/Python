from random import randint
from operator import itemgetter
lista = {'Jogador 1': randint(1,6),'Jogador 2': randint(1,6),
         'Jogador 3':randint(1, 6),'Jogador 4':randint(1,6)}
ranking = dict()
print('Ranking')
ranking = sorted(lista.items(),key = itemgetter(1),reverse =True)
for indece, valores in enumerate(ranking):
    print(f' {indece+1}° lugar o {valores[0]} com {valores[1]}')