from datetime import date
atual = date.today().year
dataDeNascimento = int(input('Informe a data de nascimento : '))
if (atual-dataDeNascimento)<=9:
    print('Mirim')
elif (atual-dataDeNascimento)<=14:
    print('Infantil')
elif (atual-dataDeNascimento)<=19:
    print('Junior')
elif (atual-dataDeNascimento)<=25:
    print('Sênior')
else:
    print('Master')