totalDeMulheres = 0
maior = 0
nomeDoMaisVelho = ''
media = 0
for contadora in range (1,5):
    print ('Pessoa N° {} '.format(contadora))
    nome = str(input('Informe o nome da pessoa : '))
    idade = int(input('Quantos anos de idade : '))
    media = (media+ idade)/contadora
    print('\n Escolha o numero do sexo : ')
    print('[1] para Mulher')
    print('[2] para Homem')
    sexo = int(input('Digite o numero escolhido : '))
    if sexo == 1:
        if idade<20:
            totalDeMulheres += 1
    elif sexo == 2:
        if idade > maior:
            maior = idade
            nomeDoMaisVelho = nome
print('A media de idade é',media)
print('No total de mulheres de menos 20 anos são',totalDeMulheres)
print('{} e mais velho com a idade de {}'.format(nomeDoMaisVelho,maior))