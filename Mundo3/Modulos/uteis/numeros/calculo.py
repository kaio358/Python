def fatorial(numero):
    valor = 1
    for contador in range(1,numero+1):
        valor *= contador
    return valor