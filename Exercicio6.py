#Você define um número de 1 á 5 e o mágico tenta acertar.
import random

def main():
  print('Número mágico')
  seu_numero = random.randint(1,5)
  print(seu_numero)
  numero_magic = int(input('O seu númeoro é: '))
  if numero_magic == seu_numero:
    print('O mágico acertou meu número')
  elif numero_magic > seu_numero:
    print('O mágico precisa diminuir o chute')
  else:
    print('O mágico precisa aumentar o chute')
main()