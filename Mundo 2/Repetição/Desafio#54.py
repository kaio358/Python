from datetime import date

anoAtual = date.today().year
totalDePessoasMaior = 0
totalDePessoasMenor = 0
for contadora in range (1,8):
    anoDeNascimento = int(input('Informe o ano de nascimento : '))
    if (anoAtual-anoDeNascimento)>=18:
        print('Maior de idade')
        totalDePessoasMaior += 1
    else:
        print('Menor de idade')
        totalDePessoasMenor +=1
print('No total de pessoas maior de idade são',totalDePessoasMaior)
print('No total de pessoas menor de idade são',totalDePessoasMenor)