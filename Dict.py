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

print('-----------------------------------------------------------')

def dict3():
    dict = {'palavra':1, 'palavra2':2.8, 'palavra3':'palara4'} ##Pode usar numeros nas dicts como valores
    print(dict)
    print('-----------------------------------------------------------')
    dict1 = {1:'um',2:'dois',3:'tres',4:'quatro'}##E também numeros nas chaves
    print(dict1)
    print(dict1[1])##Apesar de parecer um índice, está buscando pela CHAVE denominada '1'
    for i in range(1,5):##Printa os valores com base nas chaves da dict1
        print(dict1[i])
dict3()