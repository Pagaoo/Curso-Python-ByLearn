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
list_b = list_a[:] ##Equanto na linha abaixo eu copio uma lista para a outra, aqui, referencio apenas os elementos da list_a
##list_b = list_a
list_b.append('e')
print(f'Lista_a: {list_a}')
print(f'Lista b: {list_b}')

print('---------------------------------------------')
#Mostrando os elementos da lista, um por um e fatiando listas
listaA = list([1,2,3,4,5,6,7,8,9,10])
elem1 = listaA[0]
elem2 = listaA[1]
elem3 = listaA[2]
print(elem1, elem2, elem3)
print('--------------------------------------------')
teste1 = listaA[1:4] #Mostra elementos da posição 1 até o teto 4, ou seja, mostra do número 2 até o número 4
teste2 = listaA[:7] #Mostra elementos de todas as posições até a sétima posição, mesma coisa, a posição 7 não entra pois é o teto final
teste3 = listaA[4:] #Mostra elementos da posição 4 em diante, até o final da lista
print(f'teste 1: {teste1}')
print(f'teste 2: {teste2}')
print(f'teste 3: {teste3}')
