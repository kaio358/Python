from datetime import date
ano = int(input('Informe o ano, que será analisado (valor zero será o atual) : '))
if ano ==0:
    ano= date.today().year
    
if ((ano % 4==0) and (ano % 100!=0) or (ano%400==0)):
   print('O ano {} e bissexto '.format(ano))
else:
   print('O ano {} não é bissexto'.format(ano))    