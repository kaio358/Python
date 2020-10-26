#palíndromo, farei de duas formas
frase = str(input('Insira a frase : ')).strip().upper()
palavra = frase.split()
junto =' '.join(palavra)
inverso = junto[::-1]
print(inverso)
if inverso == junto : 
    print('É palindromo')
else:
    print('Não é palindromo')