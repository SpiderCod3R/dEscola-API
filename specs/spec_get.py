import requests
import jsonpath

# VARIAVEIS PARA TESTE DAS REQUISIÇÕES
header = {'Authorization': 'Token 90fbaa5833d46f6cb04de5750fc544d2aee5c8c1'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

# GET CURSOS
response = requests.get(url=url_base_cursos, headers=header)

#Testando se o endpoint esta correto
assert response.status_code == 200

# Testando a quantidade de registros
assert response.json()['count'] == 4

# Testando se o Titulo do primeiro curso está correto
assert response.json()['results'][0]['titulo'] == 'criando-apis-rest-com-django-rest-framework-essencial'
