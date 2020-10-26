compra = float(input('Preço das compras : '))
print('Forma de pagamentos')
print('1 para a vista com dinheiro/cheque')
print('2 para a vista com cartão')
print('3 para 2X no cartão')
print('4 para 3x ou mais no cartão \n')
opcao = int(input('A sua opção : '))
if (opcao == 1):
    print('Valor que será pago :',compra-(compra*0.10))
elif opcao == 2:
    print('Valor que será pago :',compra-(compra*0.05))
elif opcao == 3:
    print('Valor que será pago por mês {}, no valor total {}'
          .format(compra/2,compra))
elif opcao == 4:
    vezes = int(input('Quantas vezes será pago : '))
    print('Valor que será pago por mês {},no valor total {}'
          .format((compra+compra*0.20)/vezes,compra+compra*0.20))   
else:
     print('Invalido a opção')   