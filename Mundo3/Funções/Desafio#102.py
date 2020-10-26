def fatorial(numero,show = False):
    """
    

    Parametros
    ----------
    numero : Inteiro
         o numero a ser fatoriado.
    show : Booleano, opcional
        Mostrar o calculo ou não.

    Returns
    -------
    fator : Inteiro
        Retornará o valor ja calculado.

    """
    fator = 1
    for contador in range (numero,0,-1):
        if show:
            print(contador,end = '')
            if contador > 1:
                print(' X ',end = '')
            else:
                print(' = ',end = '')
        fator *= contador
    return fator
print(fatorial(int(input('Insira o valor do fatorial : '))
               ,bool(input('True ou False '))))