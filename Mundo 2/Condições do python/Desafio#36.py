valorDaCasa = float(input('Valor da Casa : '))
salario = float(input('Salario do comprador : '))
anoDeFinanciamento = int(input('Insira o ano de financiamento : '))
print('\nO valor do financiamento mensal é {:.2f}'.format
      (valorDaCasa/(anoDeFinanciamento*12)))
if(salario*0.30)>(valorDaCasa/(anoDeFinanciamento*12)):
    print('\nFinanciamento aceito !!')
else:
    print('\nFinanciamento negado!!')