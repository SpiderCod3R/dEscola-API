import requests

# VARIAVEIS PARA TESTE DAS REQUISIÇÕES
headers = {'Authorization': 'Token 4843683725a02d07d99151818ca41408c06f7284'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}5/', headers=headers)

# Testando o Status Code HTTP:204
assert resultado.status_code == 204

# Testando se o Tamanho do Conteudo retornado é 0 (zero)
assert len(resultado.text) == 0
