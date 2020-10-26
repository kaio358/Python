listaDePalavras = ('Aprender','Programar','Linguagem','Python','Curso','Gratis',
                   'Estudar','Praticar','Trabalhar','Mercado','Programador',
                   'Futuro')
for palavras in listaDePalavras:
    print(f'\n A palavra {palavras} temos', end=' ')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print(letras.lower(),end=' ')