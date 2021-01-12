#Usar duas funções para calcular a média, uma para receber as notas e a outra para calcular a média
def recebe_Notas():
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    return media(n1,n2)

def media(n1,n2):
    media = (n1 + n2) / 2
    return media
minha_media = recebe_Notas()##A função recebe 2 parametros, logo a def media() não poderia ser alocada aqui, já que retorna a media pra recebe_Notas e lá possui 2 parametros
print(f'A media do aluno é de: {minha_media}')