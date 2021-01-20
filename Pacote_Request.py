# Trabalha com requisições de páginas html
import requests

resposta = requests.get('https://google.com')
print(resposta)  # Retorna um status Code -> Informa o tipo de resposta, o 200 significa que a requisição funcionou
# 200 -> Deu certo
# 404 -> Não achada a página

print('Status:\n', resposta.status_code)

# Verificar encoding
print('\nEncdoing\n', resposta.encoding)

# Pegar os headers
print('\nHeaders\n', resposta.headers)

# Pegar conteúdos do site
print('\nConteúdos\n', resposta.content)