peso = float(input('Informe o peso : '))
altura = float(input('Informe a altura : '))
imc = peso/(altura**2)
if (imc<18.5):
    print('A baixo do peso')
elif (imc>=18.5)and(imc<25):
    print("Peso ideal")
elif 25<=imc<30 : 
    print('Sobrepeso')
elif 30<=imc<40:
    print('Obesidade')
elif imc>=40:
    print('Obesidade Mórbida')
