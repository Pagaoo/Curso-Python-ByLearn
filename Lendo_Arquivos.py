f = open('Arquivos//arquivo.txt')  # Read -> Leitura de arquivos
print(f)

print(f.read())  # Vai ler todo o arquivo
print(type(f.read()))  # f.read() é um str
# O f.readline() lê uma linha por execução. Existe também o readlines() que transforma os items do arquivo em uma lista
f = open('Arquivos//arquivo2.txt')
linhas = f.readlines()  # a função retorna as linhas restantes do arquivo, caso já tenham sido lidas todas, retorna uma lista vazia
print(linhas)