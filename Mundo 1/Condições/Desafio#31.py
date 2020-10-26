distancia = float(input('Insira a distacia da viagem : '))
preco = distancia*0.50 if distancia <= 200 else distancia*0.45
print ('A passagem custará :',preco)