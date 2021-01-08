##Dicionarios aninhados
def Est1():
    cursos = {'Javascript':{'nome': 'Aprenda Javascript', 'categoria': 'contrução de aplicativos', 'instrutor': 'Gabriel', 'alunos': 1500},
               'Python':{'nome': 'aprenda python', 'categoria': 'criação de programas', 'instrutor': 'Amanda', 'alunos': 6230},
               'Docker':{'nome': 'Docker, usando containers', 'categorias': 'programação', 'instrutor': 'Gabriel', 'alunos': 500}
             }
    for chave in cursos.keys():
        print(chave)
    print(cursos['Python']['nome'])
Est1()
print('-'*25)
##Listas aninhadas
def Est2():
    list = [[1,2,3,4,5], [1.2, 2.3, 3.4, 4.5, 5.6], ['abc', 'def', 'ghi']]
    print(list)
    print(list[1])
    print(list[1][3])
Est2()
print('-'*25)
##Tuplas aninhadas
def Est3():
    tuple = ((1,2), (3.4, 4.5), ('a', 'b'), ('ABC', 'DEF'))
    print(tuple)
    print(tuple[3])
    print(tuple[3][1])
    print(tuple[3][1][1:])##Como são str posso pegar uma parte apenas  delas
Est3()
