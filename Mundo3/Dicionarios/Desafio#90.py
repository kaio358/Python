aluno = {}
aluno ['nome'] = str(input('Informe o nome do aluno : '))
aluno ['Media'] = float(input('Informe a media : '))
if aluno['Media'] >= 7 : 
    aluno ['situação'] = 'Aprovado'
elif 5<= aluno['Media'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['Media'] <5:
    aluno['situação'] = 'Reprovado'
print('-'*30)
for chave,valores in aluno.items():
    print(f' -{chave} é igual a {valores}')