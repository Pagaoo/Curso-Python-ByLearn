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
print('-----------------------------------------------')
#Juntando listas(JOIN)
lista_id1 = [1,2,3,4]
lista_id2 = [9,15,24]
lista_id3 = [11,15]
lista_ids = lista_id1 + lista_id2 + lista_id3
print(lista_ids)
print('-------------------------------------------------')

#Funções presentes nas listas
##Append() -> adiciona um novo elemento na lista sempre no final da lista
##Index() -> Mostra o index de um elemento da lista
cursos = ['Python', 'Js', 'HTML']
index_Js = cursos.index('Js')
print(f'O indice do curso de Js é de: {index_Js}')
print(cursos.index('HTML'))
print('--------------------------------------------')
##Insert() -> Insere um elemento na lista em uma determinada posição
animais = ['Gato', 'Dog', 'Furão']
animais.insert(0,'Peixe')
print(animais)
print('-----------------------------------------------')
##In() -> Indica se o elemente está ou não na lista. (Não server só para uso em listas)
cursos_alunos = ['Rafael', 'Roberta', 'Judite']
checar = 'Aluno' in cursos_alunos
print(checar)
print('--------------------------------------------------------')
##Remove() -> Remove um elemento determinado
animais = ['Gato', 'Dog', 'Furão']
animais.insert(0, 'Peixe')
print(animais)
animais.remove('Furão')
print(animais)
print('-----------------------------------------------')
##Pop() -> Remove um elemento em um determinado indice, utilizando o indice passado, sem ver o que é o elemento
animais = ['Gato', 'Dog', 'Furão']
animais.insert(0, 'Peixe')
print(animais)
animais.pop(2)
print(animais)
print('------------------------------------------------')
##Del()-> Remove um elemento em um determinado indice, interagindo com o elemento em si e o indice
animais2 = ['Gato', 'Dog', 'Furão', 'Leão']
del(animais2[2])
print(animais2)
print('------------------------------------------------')
##Sort() -> Ordena os elementos da lista, interage diretamente na lista, não retorna nada
lista_num = [11, 1, 15, 9, 2]
print(lista_num)
lista_num.sort()
print(lista_num)
lista_abc = ['c', 'f', 'h', 'a']
print(lista_abc)
lista_abc.sort()
print(lista_abc)
print('--------------------------------------------------')
##Utilizando sorted()
lista_num2 = [15, 3, 90, 8]
print(sorted(lista_num2))
print('--------------------------------------------------')

##Jeito simplificado de programar lista com laço de repetição 'for'
print('Jeito normal de declarar lista')
listas = []
for i in range(11):
  lista.append(i)
print(lista)
print('Jeito simplificado')
lista1 = [i for i in range(11)]
print(lista1)