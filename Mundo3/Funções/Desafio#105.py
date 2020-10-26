def notas(*valor,situacao =False):
    """
    

    Parameters
    ----------
    *valor : composta
          É uma variavel dinamica, onde recebera o valor do usuario.
    situacao : Booleano, opcional
        A variavel tem a função de mostra a situação do aluno,ao colocar 
        verdadeiro, se for falso não vai mostrar.

    Returns
    -------
    boletim : dicionario
        Retornará o resultado dos valores analisado e suas expectivamente os
        locais.

    """
    boletim = {}
    boletim ['Total de notas '] = len(valor)
    boletim ['Maior'] = max(valor)
    boletim['Menor'] = min(valor)
    boletim['Media'] = sum(valor)/len(valor)
    if situacao:
        if boletim['Media'] >= 7:
            boletim['Resultado'] ='BOA!!!'
        elif 5<=boletim['Media']<7:
            boletim['Resultado'] = ' REGULAR'
        elif boletim['Media']< 5:
            boletim['Resultado'] = ' RUIM!!!'
    return boletim

informar = notas(8,3,7,situacao = True)
print(informar)