#Sequência de Fibonacci
termos = int(input('Insira a quantidade de termos : '))
contadora = 0
primeiroTermo=0
segundoTermo = 1
print('{} -> {} ->'.format(primeiroTermo,segundoTermo),end = ' ')
terceiroTermo = 0
while contadora <=termos:
    terceiroTermo = primeiroTermo+segundoTermo
    print(terceiroTermo,'->',end=' ')
    primeiroTermo = segundoTermo
    segundoTermo = terceiroTermo
    contadora +=1
print('Fim')
   