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