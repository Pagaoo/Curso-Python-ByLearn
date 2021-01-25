# Criar uma classe com construtor de nome e de estado, printar o nome e o estado do carro

class Car():
    def __init__(self, estado, nome):
        self.estado = estado
        self.nome = nome
    def Mostrar_carros(self):
        print(f'O carro {self.nome} possui estado de {self.estado}')

bmw = Car('Novo', 'BMW i3')
fusca = Car('Quebrado', 'Fusca 2020')
ferrari = Car('Semi-novo', 'Ferrari California')

bmw.Mostrar_carros()
fusca.Mostrar_carros()
ferrari.Mostrar_carros()