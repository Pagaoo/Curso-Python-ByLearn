import numpy as np

# Vetor = sequência de elementos
# arange = Popula meu vetor
vetor = np.arange(20)  # 20 é exclusivo
print(f'Vetor: {vetor}')

# Cria matriz -> Reshape = Muda o formato do vetor
# 4 linhas x 5 colunos
matriz = vetor.reshape(4,5)
print(f'Matriz: {matriz}')

# Mostrar as dimensões
dim = vetor.ndim
dim2 = matriz.ndim
print(f'Dimensões do vetor: {dim} e dimensões da matriz: {dim2}')

# Operações matemáticas
print(f'Adição do vetor: {vetor+2}')
print(f'Subtração do vetor: {vetor-2}')
print(f'Multiplicação do vetor: {vetor*2}')
print(f'Divisão do vetor: {vetor/2}')
