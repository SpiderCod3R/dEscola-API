import requests
import jsonpath

# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# Todos os nomes das pessoas que avaliaram o curso
# nomes= jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(nomes)

# Todas as avaliacoes das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)
