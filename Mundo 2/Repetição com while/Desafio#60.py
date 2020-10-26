numero = int(input('Insira o seu numero : '))
fatorial = numero - 1
total = numero
while fatorial != 0 :
    print('X',fatorial,end=' ')
    total = total * fatorial
    fatorial -= 1
    
print(' = ',total)