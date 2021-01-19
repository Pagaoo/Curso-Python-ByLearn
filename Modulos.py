# Importa toda  biblioteca
import math
import random

# Importa so a função pow da biblioteca math, no caso, não se usa mais math()
# só usa-se a funnção importada pow()
from math import pow

# Modulo math, o principal das bibliotecas de matemática
# Fatorial de um numero:
fat = math.factorial(5)
# Raiz quadrada de um número:
raiz = math.sqrt(25)
# Cosseno de um número em radianos:
cos = math.cos(906)
# Valor de pi:
pi = math.pi
# Valor de Euler:
e = math.e
print(f'Fatorial de 5 = {fat}')
print(f'Raiz de 25 = {raiz}')
print(f'O cosseno de 90 em radianos é: {cos}')
print(f'Valor de pi = {pi}')
print(f'Valor de Euler = {e}')
