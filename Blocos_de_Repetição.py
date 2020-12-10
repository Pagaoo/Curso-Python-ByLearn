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
