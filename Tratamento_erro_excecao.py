# Para evitar que exceções ocorram podemos realizar tratamentos prévios.
# Sendo assim, tentamos prever o erro e evitar que aconteça ou avisar ao usuário sobre esse erro

try:
    n = int(input('Número: '))  # Tento isso
except ValueError:
    print('Coloque apenas números inteiros')  # Se der erro, mostra isso
else:
    print(n)  # Se não der erro, faça isso

print('-'*50)

try:
    n_2 = int(input('Número: '))
    m = int(input('Número: '))
    x = n_2 / m
except (ZeroDivisionError, ValueError):  # Dá para juntas as exceções em uma tupla ou usar duas funções except
    print('Erro: Coloque números inteiros diferentes de zero!!!!')