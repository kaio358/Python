numero = ('zero','um','dois','três','quatro','cinco','seis','sete',
          'oito','nove','dez','onze','treze','catorze','quinze','dezesseis',
          'dezessete','dezoito','dezenove','vinte')
valor = -1
while True:
    valor = int(input('Insira o numero : '))
    if 0 <= valor <=20:
        break
print(f'O valor digitado foi {numero[valor]}')