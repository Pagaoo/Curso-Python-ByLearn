##O exercicio consiste em printar os numeros pares e parar a execução quando chegar ao numero 15
def Exercicio8():
    for i in range(20):
        if (i == 15):
            break
        if (i %  2 != 0):
            continue
        print(i)
Exercicio8()