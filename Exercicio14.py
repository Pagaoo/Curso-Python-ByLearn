# Media com try/except
class Aluno():
    status = False


    def __init__(self, nome):
        self.nome = nome

    def Notas(self, nota1, nota2):
        try:
            self.nota1 = float(nota1)
            self.nota2 = float(nota2)
        except ValueError:
            print('Inserir números nas notas')
    
    def Media(self):
        try:
            return (self.nota1 + self.nota2) / 2
        except AttributeError:
            print('Notas não informadas')

    def aprovado_Reprovado(self):
        try:
            status = (self.Media() >= 6)
            if(status):
                print(f'O aluno {self.nome} foi aprovado')
            else:
                print(f'O aluno {self.nome} foi reprovado')
        except TypeError:
            print('Notas não informadas')

Aluno1 = Aluno('Gabriel')
Aluno1.Notas(9,6)
Aluno1.Media()
Aluno1.aprovado_Reprovado()
