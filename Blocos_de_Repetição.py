alunos = ['Amanda', 'Gabriel', 'Roberta']

alunos.append('Anderson')

for aluno in alunos:
    print(aluno)

print('----------------------------------------------')

##Matriz:
lista = [[1,2], [3,4]]
print(lista[0])
print(lista[0][0])
print(lista[1][0])

print('----------------------------------------------')

##Laço de repetição (While)
def whileMain():
    i = 1
    while i < 6:
        print(i)
        i += 1
whileMain()

print('----------------------------------------------')

##Não se itera int, precisa ser em um intervalo
def while2():
    i = '0'
    while i != '9':
        i = input('Digite um número: ')
        for j in range(1,int(i) + 1):
            print('O número digitado é:', j)
while2()

print('----------------------------------------------')

##Continue e Break, os dois funcionam com o for também
##O continue segue para a proxima etapa se uma condição for preenchida
def break1():
    i = 1
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            break
break1()

print('----------------------------------------------')

def continue1():
    i = 0
    while i < 10:
        i += 1
        if (i == 3):
            continue
        print(i)
continue1()

print('----------------------------------------------')

##EXTRA: Há else em blocos de repetição

def forex():
    for i in range(5):
        print(i)
    else:
        print('Após laço e iteração')
forex()

print('----------------------------------------------')

def whileEx():
    i = 1
    while i < 5:
        print(i)
        i += 1
    else:
        print('i não é menor que 5 mais')
        print(i)
whileEx()