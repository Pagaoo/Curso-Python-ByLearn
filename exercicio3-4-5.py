def multiplicacao():
  print('Multiplicação de dois números')
  x = float(input('Digite o primeiro número: '))
  y = float(input('Digite o segundo número: '))
  mult = x * y
  print(f'A multiplicação de {x} e {y} é {mult}')
multiplicacao()

print('------------------------------------')

def divisao():
  print('Divisão de dois números')
  a = float(input('Digite o primeiro número: '))
  b = float(input('Digite o segundo número: '))
  div = a / b
  print('A divisão de {0} com {1} é de: {2}'.format(a,b,div))
divisao()

print('-----------------------------------------')

def subtracao():
  print('Subtração de dois números')
  q = float(input('Digite o primeiro número: '))
  w = float(input('Digite o segundo número: '))
  sub = q - w
  print('A subtração de {0} com {1} é de {2}'.format(q,w,sub))
subtracao()
