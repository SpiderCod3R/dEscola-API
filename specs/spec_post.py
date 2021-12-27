import requests
import jsonpath

# VARIAVEIS PARA TESTE DAS REQUISIÇÕES
headers = {'Authorization': 'Token 90fbaa5833d46f6cb04de5750fc544d2aee5c8c1'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com SCRUM",
    "url": "https://geekuniversity.com.br/scrum",
}

resultado = requests.post(url= url_base_cursos, headers=headers, data=novo_curso)

# Testando o STATUS CODE HTTP: 201

assert resultado.status_code == 201

#testando se Titulo do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
