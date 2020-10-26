import moeda

valor = float(input('Informe o valor R$ : '))
print(moeda.cifrao(moeda.aumentar(valor,float(input('Informe a taxa :')))))

print(moeda.cifrao(moeda.diminuir(valor,float(input('Informe a taxa :')))))

print(moeda.cifrao(moeda.metade(valor)))

print(moeda.cifrao(moeda.dobro(valor)))
