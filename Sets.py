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
    conjunto2 = {'a','j','e','h','x','d'}
    print('Conjunto 1:',conjunto)
    print('Conjunto 2:',conjunto2)
    conjunto.add('g')
    conjunto2.add('z')
    print('Conjunto 1 modificado:',conjunto)
    print('Conjunto 2 modificado:',conjunto2)
    conjunto_total = conjunto.union(conjunto2) ##Une (soma) os conjuntos escolhidos. O union retorna um valor (conjunto)
    print('Conjunto total:',conjunto_total)
conjuntos()

print('--------------------------------------------------------')

def frutas():
    frutas = {'Apple', 'Orange'}
    frutas.update(['Pineapple', 'Apricot', 'Ackee'])##Adiona uma lista de elementos ao conjunto, também une dois conjuntos, mas adiciona direto ao conjuto. Ex: frutas.uptade(frutas2)
    frutas.remove('Apple') ##Remove uma chave do conjunto, se o elemento não existir dará erro
    frutas.discard('Pineapple')##Usando o discard, se o elemento não existir mais, não dará erro
    frutas.clear()##Limpa o conjunto e retorna um set(), ou seja, conjunto vazio
    print(frutas)
frutas()

print('--------------------------------------------------------')

def interseccao():
    conjunto = {'a','b','c','d'}
    conjunto2 = {'a','j','e','h','x','d'}
    conjunto_interseccao = conjunto.intersection(conjunto2)##Mostra os valores que existem em ambos
    conjunto_deferenca = conjunto.difference(conjunto2) ##Mostra os valores distintos que existem no conjunto 1 para o conjunto 2
    conjunto_deferenca2 = conjunto2.difference(conjunto)##Mostra os valores distintos que existem no conjunto 2 para o conjunto 1
    print('intersecção dos conjuntos:',conjunto_interseccao)
    print('diferença do conjunto1 para conjunto2:',conjunto_deferenca)
    print('difenrença do conjunto 2 para o conjunto 1:',conjunto_deferenca2)
interseccao()

print('--------------------------------------------------------')

def subconjunto():
    conjunto1 = {1,2,3}
    conjunto2 = {1,2,3,4,5,6,7}
    subconjunto1 = conjunto1.issubset(conjunto2) ##Retorna true or false, para caso um conjunto esteja contido em outro, retorna True e caso não esteja, retorna False
    print(subconjunto1)
subconjunto()

print('--------------------------------------------------------')
