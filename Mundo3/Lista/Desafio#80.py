lista = []
for contagem in range(0,5):
    numero = int(input('Insira o valor : '))
    if contagem == 0 or numero >lista[-1]:
        lista.append(numero)
    else:
        posterior = 0
        while posterior < len(lista):
            if numero <= lista[posterior]:
                lista.insert(posterior, numero)
                break
            posterior+=1
print(lista)