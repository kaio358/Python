import random 
nomeUm = input('Insira o nome : ')
nomeDois = input('Insira o nome : ')
nomeTres  = input('Insira o nome : ')
nomeQuatro = input('Insira o nome : ')
lista = [nomeUm,nomeDois,nomeTres,nomeQuatro]
random.shuffle(lista)
print("A lista : ")
print(lista)
