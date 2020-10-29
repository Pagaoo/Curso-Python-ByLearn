import random

a = random.randint(0,30)
b = random.randint(10,90)
soma = a + b
print(f'Soma de {a} + {b} = {soma}')

print('-------------------------------')

a = 5
b = -7
multiplicacao = a * b
print(multiplicacao)

print('------------------------------')

def main():
  a = 90
  b = 87
  soma = a + b
  print('A soma de',a, 'e', b, 'é:', soma)
main()

print('--------------------------------')

def main1():
  a = float(input('Defina o primeiro numero: '))
  b = float(input('Defina o segundo numero: '))
  soma = a + b
  print('A soma de',a, 'com', b, 'é de: ', soma)
main1()

print('-------------------------------------')

def main2():
  nome = input('Digite seu nome: ')
  sobrenome = input('Digite seu sobrenome: ')
  print('Seu nome é:', nome, sobrenome)
main2()