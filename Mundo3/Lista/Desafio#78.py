valor = [int(input('Insira o primeiro valor : ')),
             int(input('Insira o segundo valor : ')),
             int(input('Insira o terceiro valor : ')),
             int(input('Insira o quarto valor : ')),
             int(input('Insira o quinto valor : '))]
print(f'O maior é {max(valor)} na posição',end=' ')
for posicao,numero in enumerate (valor):
    if numero == max(valor):
        print(f'{posicao} ',end =' ')
print(f'\nO menor é {min(valor)} na posição',end=' ')
for posicao,numero in enumerate (valor):
    if numero == min(valor):
        print(f'{posicao} ',end =' ')