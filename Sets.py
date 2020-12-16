##Sets são conhecido por conjuntos e são inicializados com {}, a demais há a execção de criar um conjunto vazio, que seria com os ()
##Uma particularidade é que os Sets não aceitam duplicatas
set = {'Conjunto'}
print(set)
print(type(set))

print('--------------------------------------------------------')
##Prova de que não aceita duplicatas
conjunto = {1,1,3,4,5,5}
print(conjunto)

print('--------------------------------------------------------')
##Não são ordenados
##Usa-se add porque os sets vem das operações matemáticas de conjuntos
def conjuntos():
    conjunto = {'a','b','c','d'} 
    conjunto2 = {'j','e','h','x'}
    print('Conjunto 1:',conjunto)
    print('Conjunto 2:',conjunto2)
    conjunto.add('g')
    conjunto2.add('z')
    print('Conjunto 1 modificado:',conjunto)
    print('Conjunto 2 modificado:',conjunto2)
conjuntos()