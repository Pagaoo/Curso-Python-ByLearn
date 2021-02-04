def openarquivo():
    f = open('Arquivos//arquivo3.txt', 'a')  # Abre o arquivo e o 'a' adiciona conteúdo ao arquivo, diferentemento do 'w' que apaga o o conteúdo do arquivo e reescreve
    f.write('\nCabeção')

def ler():
    f = open('Arquivos//arquivo3.txt')
    linhas = f.readlines()
    print(linhas)
    f.close()  # Fecha o arquivo

openarquivo()
ler()