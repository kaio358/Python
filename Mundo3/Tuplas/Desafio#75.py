valores = (int(input('Informe o primeiro valor : ')),
           int (input('Informe o segundo valor : ')),
           int(input('Informe o terceiro valor : ')),
           int(input('Informe o quarto valor : ')))
print('Valores de uma tupla : ',valores)
print('o numero 9 apreceu : ',valores.count(9))
print(f'O numero 3 apareceu na posição {valores.index(3)+1}' if 3 in valores 
      else 'Valor 3 não encontrado')
print('Numeros par foi ',end='')
for numero in valores:
    if numero % 2== 0:
        print(numero,end =' ')