primeiro = int(input('Informe o termo : '))
razao = int(input(' Informe a a razão : '))
decimo = primeiro +(10-1)*razao 
for numero in range (primeiro,decimo,razao):
    print(numero,end=' ')