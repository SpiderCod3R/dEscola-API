import requests

# GET Avaliacoes

# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

# Acessando o codigo de Status da Requisição
# print(avaliacoes)

# Acessando os dados da Resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json())) Imprime o tipo dos dados

# Acessando a quantidade de reqistros
# print(avaliacoes.json()['count'])

# Acessando a próxima pagina de resultados
# print(avaliacoes.json()['next'])

# Acessando os Resultados da Pagina
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o 1º elemento da Lista de Resultados
# print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da Lista de Resultados
# print(avaliacoes.json()['results'][-1])

# Acessando o somente o nome da Pessoa da ultima Avaliação de Resultados
# print(avaliacoes.json()['results'][-1]['nome'])

# ----------------------------------------- x ----------------------------------------

# GET Avaliacao

# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')
# print(avaliacao.json())

# GET Cursos

header = {'Authorization': 'Token 90fbaa5833d46f6cb04de5750fc544d2aee5c8c1'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=header)

print(cursos.status_code)
print(cursos.json())

