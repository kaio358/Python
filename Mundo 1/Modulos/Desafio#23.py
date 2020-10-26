numero = int(input(' Informe o numero : '))
unidade = numero//1 % 10
dezena = numero//10 % 10
centena = numero//100 % 10
milhar = numero//1000 % 10 
print ('Unidade(s) : ',unidade)
print ('Dezena(s) : ',dezena)
print ('Centena(s) : ',centena)
print ('Milhar(es) : ',milhar)