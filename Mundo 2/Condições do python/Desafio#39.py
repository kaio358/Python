from datetime import date
atual = date.today().year
dataDoNascimento = int(input('Insira a data de nascimento : '))
if(atual-dataDoNascimento)<18:
    print('Ta safe, falta',18-(atual-dataDoNascimento))
elif (atual-dataDoNascimento)>18:
    print('Está atrasado para se alistar em',(atual-dataDoNascimento)-18)
else:
    print('Tem que se alistar nesse ano')