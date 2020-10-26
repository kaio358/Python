nome = str(input('Informe o seu nome : ')).strip()
print('A letra (a) tem no total de',nome.lower().count('a'))
print('A primeira letra (a) é',nome.lower().find('a')+1)
print('A ultima letra (a) é',nome.lower().rfind('a'))