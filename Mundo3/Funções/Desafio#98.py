from time import sleep
def contador (inicio,fim,passo):
    if passo <0:
        passo *=-1
    if passo == 0:
        passo = 1
    if inicio< fim:
        for cont in range (inicio,fim+1,passo):
            print(cont,end =' ')
            sleep(0.5)
        print()
    else:
        for cont in range(inicio,fim-1,-passo):
            print(cont,end =' ')
            sleep(0.5)
contador(1,10,1)
contador(10,0,2)
contador(int(input('Inicio: ')),int(input('Fim: ')),int(input('Passo: ')))