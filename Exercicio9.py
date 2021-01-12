#Fazer função para calcular a média de duas notas entradas pelo usuário
def media():
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    return media
media_aluno = media()
print(f'O aluno possui media de {media_aluno}')