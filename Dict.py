##Os dicionarios são compostos por suas chaves e respectivos valores
##Não aceitam duplicatas, e se houver chaves iguais com valores diferentes, o valor apresentado é o ultimo colocado
##É uma estrutura mutável

def dict1():
    dict = {'dog':'cachorro', 'cat':'gato', 'dog':'cachorro', 'dog':'peixe'}
    print(dict)
    print(type(dict))
dict1()

print('-----------------------------------------------------------')

def dict2():
    dict = {'dog':'cachorro', 'cat':'gato', 'bird':'passaro', 'fish':'peixe'}
    print(dict['bird']) ##Não suporta o acesso por índices, mas sim pelas chaves
    print(dict.get('bird')) ##Outra maneira de acessar os valores da dict
dict2()