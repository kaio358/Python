dinheiro = int(input('Informe a quantia de dinheiro : '))
resto = 0
notasDeCinquenta = 0
notasDeVinte = 0
notasDeDez = 0
notasDeCinco = 0
notasDeDois = 0
moedaDeUm = 0
while True :
    if dinheiro //50 >0:
        resto = dinheiro % 50
        notasDeCinquenta = dinheiro//50
    if resto // 20 > 0:
        notasDeVinte = resto//20
        resto  %= 20
    if resto // 10 > 0:
        notasDeDez = resto//10
        resto %= 10
    if resto // 5 > 0 :
        notasDeCinco = resto //5
        resto %= 5
    if resto // 2 > 0 :
        notasDeDois = resto //2
        resto %= 2
    if resto // 1 > 0 :
        moedaDeUm = resto //1
        resto %= 1
    break
print('Notas de R$ 50 :',notasDeCinquenta)
print('Notas de R$ 20 :',notasDeVinte)
print('Notas de R$ 10 :',notasDeDez)
print('Notas de R$ 5 :',notasDeCinco)
print('Notas de R$ 2 :',notasDeDois)
print('Moedas de R$ 1 :',moedaDeUm)