import requests

# VARIAVEIS PARA TESTE DAS REQUISIÇÕES
headers = {'Authorization': 'Token 4843683725a02d07d99151818ca41408c06f7284'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Microserviços com Django Rest Framework do Zero ao Mestre dos Microserviços",
    "url": "https://geekuniversity.com.br/msdrf-mestre",
}

# Buscando o Curso com ID 5
curso = requests.get(url=f'{url_base_cursos}5/', headers=headers)
assert curso.json()['titulo'] == "Gerência Ágil de Projetos com SCRUM"

resultado = requests.put(url=f'{url_base_cursos}5/', headers=headers, data=curso_atualizado)

print(resultado.json())

#Testando o STATUS CODE 200
assert resultado.status_code == 200

# Testando se o Titulo retornado bate com o titulo informado
assert resultado.json()['titulo'] == curso_atualizado['titulo']


