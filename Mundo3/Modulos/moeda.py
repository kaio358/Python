def aumentar(preco,taxa):
    valor = preco+(preco*(taxa/100))
    return valor


def diminuir (preco,taxa):
    valor = preco - (preco*(taxa/100))
    return valor


def metade (preco = 0):
    valor = preco/2
    return valor


def dobro(preco = 0):
    valor = preco*2
    return valor

def cifrao(preco = 0,nota = 'R$'):
    return f'{nota} {preco: .2f}'.replace('.',',') 
