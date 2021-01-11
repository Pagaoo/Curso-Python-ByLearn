def ola(nome):
    print('Olá,',nome)
ola('Gabriel')

print('-'*25)

def ola_idade(nome,idade):
    print(f'Olá {nome}, você tem {idade} anos!')
ola_idade('Gabriel', 21)

print('-'*25)

def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
minha_media = media(8,6)
print(f'A media do aluno é de: {minha_media}')