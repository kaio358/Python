informacao = input("Insira a informação : ")
print("Tipo primitivo : ",type(informacao))
print("Só tem espaço : ",informacao.isspace())
print("Só numero : ",informacao.isnumeric())
print("É  alfabetico : ",informacao.isalpha())
print("É Numero + alfabeto : ",informacao.isalnum())
print("Está em maisuculo : ",informacao.isupper())
print("Está en minusculo : ",informacao.islower())
print("Esta capitalizado : ",informacao.istitle())