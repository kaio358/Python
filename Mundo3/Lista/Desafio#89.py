aluno = []
classe = []
contador = 0
media = 0
continuar = 's'
mostre = 0
while continuar not in 'Nn':
  aluno.append(str(input('Informe o nome do aluno : ')))
  aluno.append(float(input('Informe a primeira nota : ')))
  aluno.append(float(input(' Informe a segunda nota : ')))
  classe.append(aluno[:])
  aluno.clear()
  contador += 1
  continuar = input('Continuar [S/N] ?')
print('-'*20)
print('Notas finais : ')
print('-'*20)
for vezes in range(0,contador):
    media = (classe[vezes][1]+classe[vezes][2])/2
    print(f'{vezes}  {classe[vezes][0]}  {media:}')
while continuar not in 'Ss':
    mostre = int(input('Informe o numero do aluno : '))
    print(classe[mostre])
    continuar = input('Sair [S/N] ?')