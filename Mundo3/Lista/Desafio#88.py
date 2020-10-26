from random import randint
valor = int(input('Informe a quantidade de vezes vai jogar : '))
lista=[]
tabela = []
numero = 0
for jogada in range (0,valor+1):
    for vezes in range (0,valor+1):
      numero = randint(1,60)
      if (numero not in lista):
        lista.append(numero)
    tabela.append(lista[:])
    lista.clear()
    tabela[jogada].sort()
    print(tabela[jogada])