class Aluno():
    status = False


    def __init__(self, nome):
        self.nome = nome

    def Notas(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
    
    def Media(self):
        return (self.nota1 + self.nota2) / 2

    def aprovado_Reprovado(self):
        status = (self.Media() >= 6)
        if(status):
            print(f'O aluno {self.nome} foi aprovado')
        else:
            print(f'O aluno {self.nome} foi reprovado')

Aluno1 = Aluno('Gabriel')
Aluno1.Notas(9,6)
Aluno1.Media()
Aluno1.aprovado_Reprovado()
