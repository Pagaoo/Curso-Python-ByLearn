class Car(object):
    comprado = False

    def __init__(self, modelo, estado, ano):
        self.modelo = modelo
        self.estado = estado
        self.ano = ano

    def Comprar(self):
        if(self.comprado):
            print('Carro já comprado')
            return
        
        self.comprado = True
        print('Carro comprado')

    def testeDrive(self):
        if(not self.comprado):
            print('Teste Drive')
            self.ligaDesliga(True)
            print('Está dirigindo')
            if(self.Acelerar()):
                print('Está tentando roubar o carro')
            else:
                print('Não pode roubar o carro')
            self.ligaDesliga(False)
            print('Não está mais dirigindo')
        else:
            print('Se comprado não pode fazer o teste drive')
    def Dirigir(self):
        if(self.comprado):
            print('Começar a dirigir o carro')
            self.ligaDesliga(True)
            print('Está dirigindo')
            if(self.Acelerar()):
                print('Está acelerando')
            else:
                print('Não pode roubar o carro')
            self.ligaDesliga(False)
            print('Não está mais dirigindo')
        else:
            print('Só pode dirigir depois de comprar o carro')
    def Acelerar(self):
        return self.comprado  # Retorna True se for True e False se for False, como se fosse um if   
    def ligaDesliga(self, status):
        if status:
            print('Carro ligado')
        else:
            print('Carro desligado')

ferrari = Car('Enzo Ferrari', 'Novo', '2007')
bmw = Car(modelo='BMW I8', estado='Semi-Novo', ano='2017')

