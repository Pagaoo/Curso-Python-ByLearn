class Car(object):
    estado = 'novo'

fusca = Car()
fusca.estado = 'novo'
ferrari = Car()
ferrari.estado = 'Usado'
print(f'Estado do fusca: {fusca.estado}')
print(f'Estado da ferrari: {ferrari.estado}')