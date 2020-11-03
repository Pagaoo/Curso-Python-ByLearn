def main():
  alunos = ['Amanda', 'Gabriel', 'Roger', 'Anderson']
  print(alunos[1])
  print(alunos)
  alunos.append('Roberta')
  print(alunos)
main()

lista = [1,2,3,4,5]
lista2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['a', 'b', 2, 3] ##Permite listas mistas
lista_alunos = [] ##Inicialização de lista vazia

#Há também o método de criação de listas built in
lista = list() ##Equivale a uma lista vazia, lista = []
var = 12
lista_elementos = list(['a', 2, var]) ##Lista com as váriaveis já definidas
print(lista_elementos)

#Copiando elementos de uma lista para outra
list_a = list(['a', 'b', 'c', 'd'])
list_b = list_a
list_b.append('e')
print(f'Lista_a: {list_a}')
print(f'Lista b: {list_b}')
