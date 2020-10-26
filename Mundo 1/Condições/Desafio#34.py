salario = int(input('Insira o valor do salario : '))
print('Será aumentado para ')
print((salario*0.15)+salario if salario <= 1250 else (salario*0.10)+salario)