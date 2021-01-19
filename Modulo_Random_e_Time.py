# O módulo random trabalha com números pseudo-aleatórios
from random import random, randrange, seed

# Módulo Time - permite trabalhar com o tempo
import time

hora = time.time()

# Aqui mostra a hora do computador, formatando em HORAS, MINUTOS E SEGUNDOS
hora1 = time.strftime('%H:%M:%S')
print(hora1)

# Semente para configurar a geração dos números
# Com essa sementa, garante que os números gerados sejam diferentes,já que a semente muda,
# já que pega o tempo no computador em segundos
seed(time.time()) 

# Número aleátorio de 0 a 1
aleatorio = random()
print(aleatorio)

# Número inclusivo, entra no sort (0) - Número mínimo do range
# Número exclusivo, não entra no sort (10) - Número máximo do range

espaco = randrange(0,10)
print(espaco)

for i in range(0,10):
    espaco = randrange(-10,10)
    print(espaco, end = ', ')