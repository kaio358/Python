while True:
    numero = int (input('Insira o numero desejado : '))
    if numero < 0 :
        print('Obrigado por usar Tabuada, volte sempre!!')
        break
    else:
      print('---'*10)
      for contadora in range (1,11):
         print(f'{numero} X {contadora} = {numero*contadora}')
      print('---'*10)