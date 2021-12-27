import requests

class TestCursos:
    headers = {'Authorization': 'Token 4843683725a02d07d99151818ca41408c06f7284'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == 200

    def test_get_curso(self):
        cursos = requests.get(url=f'{self.url_base_cursos}6/', headers=self.headers)
        assert cursos.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Gerência Ágil de Projetos com SCRUM",
            "url": "https://geekuniversity.com.br/scrum",
        }
        response = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)

        assert response.status_code == 201
        assert response.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        curso_atualizado = {
            "titulo": "Novo curso de Docker do Zero ao Mestro do Docker",
            "url": "https://geekuniversity.com.br/dockermaster"
        }

        response = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=curso_atualizado)

        assert response.status_code == 200

    def test_put_titulo_curso(self):
        curso_atualizado = {
            "titulo": "Docker & Kubernets do Zero ao Mestre do Docker",
            "url": "https://geekuniversity.com.br/dockermaster"
        }
        response = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=curso_atualizado)

        assert response.json()['titulo'] == curso_atualizado['titulo']

    def test_delete_curso(self):
        response = requests.delete(url=f'{self.url_base_cursos}9/', headers=self.headers)
        assert response.status_code == 204 and len(response.text) == 0
