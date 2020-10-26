time = []
jogador = {}
jogadas =list()
resposta ='s'
while resposta in'Ss':
    jogador.clear()
    jogador['nome'] = str(input('Insira o nome do jogador : '))
    partidas = int(input('Quantas partidas jogou ? '))
    jogadas.clear()
    for contador in range (0,partidas):
         jogadas.append(int(input(f'Quantos marcou gols na partida {contador+1} : ')))
    jogador['gols'] = jogadas[:]
    jogador['total'] = sum(jogadas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Continuar [S/N] ? '))
        if resposta in 'SsNn':
            break

print('-=-'*20)
print('cod ',end='')
for listar in jogador.keys():
    print(f'{listar:<15}',end ='')
print()
print('-=-'*20)
for chave, valor in enumerate(time):
    print(f'{chave:>3} ',end='')
    for gol in valor.values():
        print(f'{str(gol):<15}',end=' ')
    print()
print('-=-'*20)

while True :
    busca = int(input('Mostrar dados qual jogador[999 para sair ] : '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro, numero não encotrado')
    else:
        print(f'Jogador {time[busca]["nome"]}')
        for indece, gols in enumerate(time[busca]['gols']):
            print(f' No jogo {indece+1} fez {gols}')
    print('-'*30)
        
        