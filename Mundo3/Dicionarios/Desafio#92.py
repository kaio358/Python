from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Informe o nome : '))
dataDeNascimento =int(input('Informe o ano de nascimento : '))
pessoa['idade'] = datetime.now().year - dataDeNascimento
pessoa['carteira de trabalho'] = int(input('Carteira de trabalho [0 para não tem] : '))
if pessoa['carteira de trabalho'] != 0:
    pessoa['ano de contratação'] =int(input('Ano de contratação : '))
    pessoa['salario'] = float(input('Informe o salario : '))
    pessoa['aposentadoria'] =pessoa['idade']+(pessoa['ano de contratação']+35)-datetime.now().year

for chave,valores in pessoa.items():
    print(chave ,':',valores)