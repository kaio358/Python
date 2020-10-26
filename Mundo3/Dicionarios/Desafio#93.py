jogador = {}
jogadas =list()
jogador['nome'] = str(input('Insira o nome do jogador : '))
partidas = int(input('Quantas partidas jogou ? '))
for contador in range (0,partidas):
     jogadas.append(int(input(f'Quantos marcou gols na partida {contador} : ')))
jogador['gols'] = jogadas[:]
jogador['total'] = sum(jogadas)     
print('-=-'*20)
print(jogador)
print('-=-'*20)
for chaves, valores in jogador.items():
    print(chaves,' : ',valores)
print('-=-'*20)
print(f'Jogador {jogador["nome"]} participou de {partidas}')
for jogos,gols in jogador.items():
    print(f'Na partida {jogos} teve {gols} gols')
print('Com total de gols',jogador['total'])