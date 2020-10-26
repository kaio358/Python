def maior (*numero):
    maiores = contadora = 0 
    for contador in numero:
        if(contadora == 0 ):
           maiores = numero[contador]
        elif  contador > maiores:
            maiores = contador
        contadora+=1
    print('Maior numero',maiores)
maior (2,43,5,4,7,4,1)