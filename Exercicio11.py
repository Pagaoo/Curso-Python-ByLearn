#Usar duas funções para calcular a média, uma para receber as notas e a outra para calcular a média
#Com essa média calculada, tem-se outra função para consultar se o aluno tem nota minima para passar
def recebe_Notas():
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    return media(n1,n2)

def media(n1,n2):
    media = (n1 + n2) / 2
    return media

def passou_Reprovou(media):
    if(media >= 7):
        print(f'O aluno passou com média de {media}')
    else:
        print(f'O aluno reprovou com média de {media}')

passou_Reprovou(recebe_Notas())##Passando função por parametro