##Tuplas são inicializadas com os (), ao contrario das listas que são inicilizadas por []
##Tuplas não aceitão atribuições ou modificações de elementos, assim como remoção dos mesmos, é uma estrutura imutável
##Bem útil quando se tem dados fixos
##É mais rápida que uma lista
def tupla():
    tupla = (1, 2, 3)
    print(tupla)
    print(tupla[1])
    print(tupla[0])
    print(tupla[2])
tupla()

print('----------------------------------------------------------')
##Para criar ou converter uma tuple, pode-se usar a função de mesmo nome: tuple()
def tuplaEx():
    tupla = tuple([i for i in range(11)])
    print(tupla)
tuplaEx()

print('----------------------------------------------------------')

lista = [1,2,3]
tupla = tuple(lista)
print(type(lista))
print(type(tupla))

print('----------------------------------------------------------')
##Para editar tuples, pode transformar a estrutura em uma lista e depois retrasnformar para uma tupla novamente
##Não é um método recomendado, pois se os dados forem ser mutáveis,, usará lista direto
tupla1 = (1,2,3,4,5)
lista1 = list(tupla1)
lista1.append(8)
lista1[0] = 'Gabi'
lista1.remove(3)
tupla1 = tuple(lista1)
print(tupla1)

print('----------------------------------------------------------')
##Entretanto há uma forma de conduzir os dados, como as listas, dicionarios e conjuntos.
tupla2 = (1,2,3,4,5)
print('Indice:',tupla2[3])
print(tupla2[1:3]) ##Exclusivo no final, não mostrará o elemento no indice 3
print(tupla2[-1])##Mostra os elementos da direita para a esquerda, nesse caso, só mostra o ultimo elemento
print('O tamanho da tupla é de:',len(tupla2))
print('O elemento 4, está na tupla?',4 in tupla2)
print('O elemento 1, não está na tupla?',1 not in tupla2)

for i in tupla2:
    print('Elemento:',i)