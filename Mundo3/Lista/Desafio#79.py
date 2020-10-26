valores = []
continuar = ''
valor =0
while continuar in 'Ss':
    valor = int(input('Insira o valor desejado : '))
    valores.append(valor)
    if valores.count(valor) > 1:
        valores.pop()
    continuar = str(input('Continuar [S/N] ? '))
valores.sort()
print(valores)