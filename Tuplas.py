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