numero = int(input('Insira o seu numero : '))

print(' 1 para converter em binario')
print(' 2 para converter em octal')
print(' 3 para converter em hexadecimal')
opcao = int(input('\n Insira sua escolha : '))
if opcao == 1:
    print('O valor convertido em binario : ',bin(numero))
elif opcao == 2:
    print('O valor convertido em octal : ',oct(numero))
elif opcao == 3:
    print('O valor convertido em hexadecimal : ',hex(numero))
else:
    print('Valor invalido')