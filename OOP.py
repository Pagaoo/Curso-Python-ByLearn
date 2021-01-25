class Car(object):
    estado = 'novo'
    
    def dirigir(self):
        self.estado = 'usado'  # Modifica o objeto que o chama, os self serve para se referir ao objeto dessa class

fusca = Car()
fusca.estado = 'novo'
ferrari = Car()
ferrari.estado = 'Usado'
print(f'Estado do fusca: {fusca.estado}')
print(f'Estado da ferrari: {ferrari.estado}')
fusca.dirigir()
print(f'Fusca depois de dirigido: {fusca.estado}')