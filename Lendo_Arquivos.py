f = open('Arquivos//arquivo.txt')  # Read -> Leitura de arquivos
print(f)
print(f.read())  # Vai ler todo o arquivo
print(type(f.read()))  # f.read() é um str
print('-'*30)
# O f.readline() lê uma linha por execução. Existe também o readlines() que transforma os items do arquivo em uma lista
f = open('Arquivos//arquivo2.txt')
linhas = f.readlines()  # a função retorna as linhas restantes do arquivo, caso já tenham sido lidas todas, retorna uma lista vazia
print(linhas)
print('-'*30)
f = open('Arquivos//arquivo3.txt')
char = f.read(30)  # Lê os caracteres do arquivo
print(char)
for l in f:
    print(l)  # Printa as linhas restantes do arquivo através do for