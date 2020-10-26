nota = float(input('Informe a primeira nota : '))
nota2 = float(input('Informe a segunda nota : '))
media = (nota+nota2)/2
if (media>= 0)and(media<5):
    print('REPROVADO!!!')
elif(media>=5)and(media<7):
    print('RECUPERAÇÃO!!!')
elif (media>=7)and(media<=10):
    print('APROVADO!!!')
else:
    print('Nota invalida!!')