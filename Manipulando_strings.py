string = 'Pagão'
print(string[3])
##Para mudar um string, podem ser fatiadas, para mudar o valor de algum indice
nova_string = string[:2] + 'l' + string[3:]
print(nova_string)
print('------------------------------------------')
palavra = 'adcdf'
print(palavra[-1])##Começa do final e mostra a última letra
print(palavra[-2])
print('--------------------------------------------')
abc = 'adcbde'
check = 'b' in abc
check2 = 'f' not in abc
print(check)
print(check2)
print('------------------------------------------')
##Concatenar strings
print('Ga'+'bri'+'el')
##Alternar upper case and low case
string = 'Ga'+'bri'.upper()+'el'
print(string)
print('--------------------------------------------')
##tamanho da stirng
string1 = 'Gabriel'
print(len(string1))
print('-----------------------------------------------')
##Checar se os caracteres são letras
checando = 'gabriel'.isalpha()
print(checando)
checando2 = '1g3e4123gfd'.isalpha()
print(checando2)
print('-----------------------------------------------')
##Remover espaços em branco do inicio e do fim
p = '       aaaaaaaaaaaaa        '
print(p.strip())
print('-----------------------------------------------')
##Juntas itens da string atráves de algo, exemplo: ','
pa = ', '.join('abc')
print(pa)