# Se o arquivo estiver em outra pasta, dar o caminho dessa pasta
f = open('Arquivos//arquivo.txt', 'r')  # r -> Read = lê o que está no arquivo
print(f)
f = open('Arquivos//arquivo.txt', 'a')  # a -> Append = Lê e adiciona texto
print(f)
# f = open('Arquivos//arquivo.txt', 'w')  # w -> Write = Escreve no arquivo, sobre escreve o arquivo
print(f)
f = open('Arquivos//arquivo2.txt', 'w+')  # Cria um arquivo caso não exista