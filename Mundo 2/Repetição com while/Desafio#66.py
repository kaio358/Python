contadora = 0
soma = 0
while True :
    numero = int (input('Insira o numero desejado [999 para sair] : '))
    if numero == 999:
        break
    contadora += 1
    soma += numero
print(f'Numeros digitados foram de {contadora} e a soma foi {soma}')